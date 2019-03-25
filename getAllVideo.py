#!/usr/bin/python3.5

import requests
import re
from lxml import html
from bs4 import BeautifulSoup


# Access from local file
url = "RAW"
page = open(url)


#soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())

#session_requests = requests.session()

#result = session_requests.post(LOGIN_URL, data = my_data)
#print(result.status_code)
#soup = BeautifulSoup(result.text, 'html.parser')
soup = BeautifulSoup(page.read(), 'html.parser')
#print(soup.prettify())
#soup = BeautifulSoup(result.text, 'html.parser')

#a = soup.find(id="murl")
#print(a)

#a_tags = soup.find_all('p', recursive=False)
#for tag in a_tags:
#  print(tag.string)



# Get All URL
stories = soup.find_all('a', href=True)
for s in stories:
  print(s['href'])


#tree = html.fromstring(result.text)
#print(tree)
#authenticity_token = list(set(tree.xpath('//input[@name="csrfmiddlewaretoken"]/@value')))[0]


