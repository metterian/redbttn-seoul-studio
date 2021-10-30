import os, requests, django
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from insta_login import InstaBot
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redbttn_home.settings")
django.setup()
from homepage.models import InstaData


INSTA_URL = "http://www.instagram.com"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PHOTO_DIR = BASE_DIR + '/static/images/instagram/'


""" Text Preprocessing """
def textPreprocess(text) -> str:
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
def html_parser(pageSource) -> object:
    parser = BeautifulSoup(pageSource, "html.parser")
    return parser

""" Get Insta Article Preview URL """
def parsePreview(div) -> str:
    preview = div.img['srcset'].split(',')[-1] # highest resolution img
    preview = preview.replace('640w', '')
    return preview

""" Get Insta Content Text """
def parseContent(URL) -> str:
    pageSource = bot.getPageSource(URL)
    soup = html_parser(pageSource)
    title = soup.title.string
    return textPreprocess(title)



def main():
    # set crawling Insta bot
    bot = InstaBot()
    bot.login()


    # parse img and text
    pageSource = bot.getPageSource()
    soup = html_parser(pageSource)
    article = soup.find("article")
    all_div = article.find_all('div',{'class':'v1Nh3'}) # Article div


    # delete existing data to maintain up-to-date
    InstaData.objects.all().delete()

    # Save data on InstaData which is django database
    for i, div in enumerate(all_div[:9]):
        URL = INSTA_URL + div.a['href']

        # get img url
        preview = parsePreview(div)
        content = parseContent(URL)

        # download preview photo
        urllib.request.urlretrieve(preview, PHOTO_DIR+'insta_img'+str(i+1)+'.jpg')

        # save Insta models
        InstaData(preview_photo=preview, link=URL, content=content).save()

    bot.close()


if __name__ == "__main__":
    main()
