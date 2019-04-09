#!/usr/bin/python3.5

import requests
import re
from lxml import html
from bs4 import BeautifulSoup


# Access from local file
#url = "RAW"
#page = open(url)

LOGIN_URL = "https://apk.tw/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
#REQUEST_URL = "https://2018.xdultraplayer.com/"
REQUEST_URL = "https://apk.tw/forum.php"

my_data = {'username': 'USERNAME', 'password': 'PASSWORD', 'quickforward': 'yes', 'handlekey': 'ls'}

session_requests = requests.session()

result = session_requests.post(LOGIN_URL, data = my_data)
soup = BeautifulSoup(result.text, 'html.parser')
#print(soup.prettify())
result = session_requests.get(REQUEST_URL)
print(result.status_code)
soup = BeautifulSoup(result.text, 'html.parser')
print(soup.prettify())

# Get All URL
#stories = soup.find_all('a', href=True)
#for s in stories:
#  print(s['href'])

