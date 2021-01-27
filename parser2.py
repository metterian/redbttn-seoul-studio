import os
import requests, django
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from insta_login import InstaBot


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redbttn_home.settings")
django.setup()
from homepage.models import InstaData


INSTA_URL = "http://www.instagram.com"


""" Text Preprocessing """
def textPreprocess(text):
    find_index = text[90:].find("요")
    find_mark = text[70:].find("!")
    if (find_mark != -1):
        return text[:(70+find_mark + 1)]
    elif find_index != -1:
        parsed_text = text[:(90+find_index+2)]
        return parsed_text

    else:
        return text

""" Beautifulsoup4 HTML Parser """
def html_parser(pageSource):
    parser = BeautifulSoup(pageSource, "html.parser")
    return parser

""" Get Insta Article Preview URL """
def parsingPreview(div):
    preview = div.img['srcset'].split(',')[-1] # highest resolution img
    preview = preview.replace('640w', '')
    return preview

""" Get Insta Content Text """
def parsingContent(URL):
    pageSource = bot.getPageSource(URL)
    soup = html_parser(pageSource)
    title = soup.title.string
    return textPreprocess(title)


# Insta Bot Initiate
bot = InstaBot()
bot.login()


# Parsing Start
pageSource = bot.getPageSource()
soup = html_parser(pageSource)
article = soup.find("article")
all_div = article.find_all('div',{'class':'v1Nh3'}) # Article div


# Delete existing data to maintain up-to-date
InstaData.objects.all().delete()


previews, contents = [], []
for div in all_div[:9]:
    URL = INSTA_URL + div.a['href']
    preview = parsingPreview(div)
    content = parsingContent(URL)
    InstaData(preview_photo=preview, link=URL, content=content).save()

bot.close()
