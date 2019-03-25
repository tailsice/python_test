#!/usr/bin/python3.5

import requests
import re
from lxml import html
from bs4 import BeautifulSoup


# Access from local file
#url = "RAW"
#page = open(url)

USEREMAIL = "tailsice@gmail.com"
PASSWORD = "tailsice"
LOGIN_URL = "https://member.xdultraplayer.com/ssologin.php"
#REQUEST_URL = "https://2018.xdultraplayer.com/"
REQUEST_URL = "https://2018.xdultraplayer.com/tag/c/中文字幕"

my_data = {'user': 'tailsice@gmail.com', 'pass': 'tailsice', 'r': '0.789703723277332'}


session_requests = requests.session()

result = session_requests.post(LOGIN_URL, data = my_data)
soup = BeautifulSoup(result.text, 'html.parser')
result = session_requests.get(REQUEST_URL)
print(result.status_code)
soup = BeautifulSoup(result.text, 'html.parser')
print(soup.prettify())

# Get All URL
#stories = soup.find_all('a', href=True)
#for s in stories:
#  print(s['href'])

