#!/usr/bin/python3.5

import requests
import sys
from lxml import html
from bs4 import BeautifulSoup

VIDEO_URL = "http://demo.xdultraplayer.com" + sys.argv[1]

session_requests = requests.session()

result = session_requests.get(VIDEO_URL)
soup = BeautifulSoup(result.text, 'html.parser')
print(soup.prettify())

# Get All URL
#stories = soup.find_all('a', href=True)
#for s in stories:
#  print(s['href'])
