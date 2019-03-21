#!/usr/bin/python3.5

import requests
import re
from lxml import html
from bs4 import BeautifulSoup


url = "RAW"
page = open(url)


USEREMAIL = "tailsice@gmail.com"
PASSWORD = "tailsice"
LOGIN_URL = "https://member.xdultraplayer.com/ssologin.php"
#REQUEST_URL = "https://2018.xdultraplayer.com/"
REQUEST_URL = "https://2018.xdultraplayer.com/tag/c/中文字幕"
VIDEO_URL = "http://2018.xdultraplayer.com/play/KWfF2sMF6CNKLnJurpvuSvlwJCI8cFQWjWXNyI6Og6OIdg0-HAMQZIkJTZflX99AMAkAfLF7szDp-NhjIK3Ct0460fFo9fIFd_iHBQ" 

my_data = {'user': 'tailsice@gmail.com', 'pass': 'tailsice', 'r': '0.789703723277332'}

#soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())

#session_requests = requests.session()

#result = session_requests.post(LOGIN_URL, data = my_data)
#print(result.status_code)
#soup = BeautifulSoup(result.text, 'html.parser')
soup = BeautifulSoup(page.read(), 'html.parser')
#print(soup.prettify())
#result = session_requests.get(REQUEST_URL)
#result = session_requests.get(VIDEO_URL)
#print(result.status_code)
#soup = BeautifulSoup(result.text, 'html.parser')
#print(soup.prettify())


pattern = re.compile(r'\.val\("([^@]+@[^@]+\.[^@]+)"\);', re.MULTILINE | re.DOTALL)
script = soup.find("script", text=pattern)
if script:
    match = pattern.search(script.text)
    if match:
        email = match.group(1)
        print(email)

#a = soup.find(id="murl")
#print(a)

#a_tags = soup.find_all('p', recursive=False)
#for tag in a_tags:
#  print(tag.string)



# Get All URL
#stories = soup.find_all('a', href=True)
#for s in stories:
#  print(s['href'])


#tree = html.fromstring(result.text)
#print(tree)
#authenticity_token = list(set(tree.xpath('//input[@name="csrfmiddlewaretoken"]/@value')))[0]


