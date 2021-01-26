import requests
import os
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redbttn_home.settings")
# import django
# django.setup()

# InstaDate import
# from homepage.models import InstaData

def text_parser(content):
    blank = content.split(':')[1]
    s = blank.strip()
    sliceed = s[1:-1]
    text = sliceed.lstrip()
    return text

def article_text_parser(article_text):
    find_index = article_text[90:].find("요")
    find_mark = article_text[70:].find("!")
    if (find_mark != -1):
        return article_text[:(70+find_mark + 1)]
    elif find_index != -1:
        parsed_text = article_text[:(90+find_index+2)]
        return parsed_text

    else:
        return article_text



def crawl(redbttn_url):
    data  = requests.get(redbttn_url)
    return  data.content

def get_article_photo(div):     #게시물 사진 반환 .jpg
    imgs = div.find('img')
    src_sets = imgs.attrs['srcset']
    parse_start = src_sets.index('480w') + 5
    parse_end = src_sets.index('640w')
    return src_sets[parse_start:parse_end]


def get_img_640w(img):     #640w 이미지 찾기
    # image_all[0].attrs['srcset'].split(',')[4]
    img_href = img.attrs['srcset']
    img_640w = img_href.split(',')[4]
    img_640w = img_640w.replace('640w', '')
    return img_640w

def get_article_href(div):     #게시물 사진 링크 반황
    a_link = div.find("a")
    article_link = a_link.attrs['href'] #게시물 링크 저장
    return article_link



def html_parer(pageSource):
    parser = BeautifulSoup(pageSource, "html.parser")
    return parser
chrome_options = Options()
# chrome_options.add_argument("--headless")



driver = webdriver.Chrome(
    executable_path= "/Users/seungjun/chromedriver/chromedriver",
    options = chrome_options
)
redbttn_url = "https://www.instagram.com/redbttnseoul/?hl=ko"
insta_url = "http://www.instagram.com"
driver.get(insta_url)
driver.implicitly_wait(3)
login_input = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
password_intput = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
login_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
id = '0514lsj@naver.com'
passwd = 'eminem6505'

login_input.send_keys(id)
password_intput.send_keys(passwd)
login_btn.click()
sleep(2)
driver.get(redbttn_url)

pageSource = driver.page_source
soup = html_parer(pageSource)
article_photo = []
article_href=[]

# article = soup.find_all("article")[1]   #인스타 게시물
article = soup.find("article")
all_div = article.find_all('div',{'class':'v1Nh3'}) #인스타 각 게시물



for div in all_div[:9]:
    href = get_article_href(div)
    article_redbttn_url = insta_url+href
    article_href.append(article_redbttn_url)

    f_photo = get_article_photo(div)
    article_photo.append(f_photo)


# InstaData.objects.all().delete()
if __name__=='__main__':

    for div in all_div[:9]:
        href = get_article_href(div)
        article_redbttn_url = insta_url + href
        pageSource = crawl(article_redbttn_url)
        parser = html_parer(pageSource)
        content = parser.find('title')
        p_content = text_parser(content.text)
        parsed_text = article_text_parser(p_content)
        f_photo = get_article_photo(div)

        InstaData(preview_photo=f_photo, link=article_redbttn_url, content=parsed_text).save()

driver.close()
