#!/usr/bin/python3.5

import requests
import sys
from lxml import html
from bs4 import BeautifulSoup


LOGIN_URL = "https://apk.tw/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
REQUEST_URL = "https://apk.tw/" + sys.argv[1]
REQUEST_URL2 = "https://apk.tw/home.php?mod=space&do=notice&view=app"

my_data = {'username': 'USERNAME', 'password': 'PASSWORD', 'quickforward': 'yes', 'handlekey': 'ls'}

session_requests = requests.session()

result = session_requests.post(LOGIN_URL, data = my_data)
result = session_requests.get(REQUEST_URL)
result = session_requests.get(REQUEST_URL2)


