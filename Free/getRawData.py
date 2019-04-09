#!/usr/bin/python3.5

import requests
import re
from lxml import html
from bs4 import BeautifulSoup


# Access from local file
#url = "RAW"
#page = open(url)

REQUEST_URL = "http://demo.xdultraplayer.com/ch1"

session_requests = requests.session()

result = session_requests.get(REQUEST_URL)
soup = BeautifulSoup(result.text, 'html.parser')
print(soup.prettify())

# Get All URL
#stories = soup.find_all('a', href=True)
#for s in stories:
#  print(s['href'])

