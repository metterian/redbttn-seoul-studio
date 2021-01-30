# Redbttn Studio Homepage
The website development of Red Button Studios in Sinsa-dong, Gangnam-gu, Korea.

Instagram: [@redbttnseoul](https://www.instagram.com/redbttnseoul/)



## Project interests
### Front-end

#### HLS Streaming
- Need real-time video streaming technology to match the self-video studio concept
- AWS CloudFront for simultaneous streaming to multiple connectors
- Video JS
#### Instagram Grid Style
- Real-time synchronized Instagram feed layout
#### Optimized for mobile(android & ios) and web
- CSS for devices which has multiple resolutions
- Video format with Android and iOS support

### Back-end
#### Crawling Bot
- Develop a crawling bot for real-time Instagram feed synchronization
- Modularize each function like a bot e.g. Log in, Crawling, Terminate
#### Server
- AWS EC2, Ubuntu 18.04
- Crontab(crawling bot with real-time scheduling)


## Dependency
<p align="left">
    <img alt="python-3.7.7" src="https://img.shields.io/badge/python-3.7.7-blue"/>
    <img alt="django-2.2.5" src="https://img.shields.io/badge/Django-2.2.5-brightgreen"/>
    <img alt="chromedriver-79.0.3945" src="https://img.shields.io/badge/chromedriver-79.0.3945-blueviolet"/>
</p>




## Installing
```
pip3 install -r requirement.txt
```

to run parser.py:
- download chromedriver, unzip, move to  `HOME_PATH`/chromedriver (mac os / linux)


create a secret.json file with variables:

```
SECRET_KEY = 'secret_key_in_settings.py'
username = 'instagram_username'
password = 'instagram_password'
```

## Runnig
to make instagram database using crawling:
```
python3 parser.py
```
to run server:
```
python3 manage.py runserver
```



## Skill
<p align="left">
    <img alt="python" src="https://img.shields.io/badge/Python- -black"/>
    <img alt="python-3.7.7" src="https://img.shields.io/badge/CSS-%20-blue"/>
    <img alt="" src="https://img.shields.io/badge/HTML-%20-orange"/>
    <img alt="javascript" src="https://img.shields.io/badge/JavaScript-%20-yellow"/>
    <img alt="hls" src="https://img.shields.io/badge/HLS-%20-red"/>
    <img alt="videojs" src="https://img.shields.io/badge/VideoJS-%20-yellowgreen"/>
    <img alt="sqlite3" src="https://img.shields.io/badge/sqlite3- -blue"/>
    <img alt="selenuum" src="https://img.shields.io/badge/selenuum- -black"/>
    <img alt="beautifulsoup4" src="https://img.shields.io/badge/beautifulsoup4- -green"/>
    <img alt="AWS" src="https://img.shields.io/badge/AWS-%20-orange"/>
</p>


## Reference
- VideoJS

    https://videojs.github.io/videojs-contrib-hls/

-  Web Scraping Instagram with Selenium | by Mariyasha | Analytics Vidhya | Medium:

    https://medium.com/analytics-vidhya/web-scraping-instagram-with-selenium-b6b1f27b885
- Automate TINDER with Python tutorial:

    https://github.com/aj-4/tinder-swipe-bot

- Django  Project Deploy - 1. AWS

    https://nachwon.github.io/django-deploy-1-aws/

- SalesMore :: Amazon AWS :: Configuring HLS Streaming with Cloudfront

    https://salesmore.tistory.com/851

