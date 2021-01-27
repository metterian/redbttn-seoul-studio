import os, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

HOME_PATH = os.path.expanduser('~')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(BASE_DIR, 'secret.json')) as f:
    secrets = json.loads(f.read())

INSTA_URL = "https://www.instagram.com/accounts/login/"
REDBTTN_URL = "https://www.instagram.com/redbttnseoul/?hl=ko"

class InstaBot():
    def __init__(self, headless=False) -> None:
        # Selenium Settings
        chrome_options = Options()
        if headless: chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(
            # chromedriver path
            executable_path= os.path.join(HOME_PATH, "chromedriver/chromedriver"),
            options = chrome_options
        )

    def login(self) -> None:
        # Open url
        self.driver.implicitly_wait(3)
        self.driver.get(INSTA_URL)

        # Login
        username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

        username.clear()
        username.send_keys(secrets['username'])

        password.clear()
        password.send_keys(secrets['password'])
        Login_bttn = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


        # Handling pop-up messages
        not_now = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
        not_now2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


    # Get page source from url
    def getPageSource(self, URL = REDBTTN_URL) -> str:
        self.driver.get(URL)
        pageSource = self.driver.page_source
        return pageSource

    # Get article title
    def getArticleText(self, URL):
        self.driver.get(URL)



    def close(self) -> None:
        self.driver.quit()



