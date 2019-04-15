#!/usr/bin/python3.5

import requests
import re
from lxml import html
from bs4 import BeautifulSoup


LOGIN_URL = "https://apk.tw/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
REQUEST_URL = "https://apk.tw/forum.php"
REQUEST_URL2 = "https://apk.tw/home.php?mod=space&do=notice&view=system"
REQUEST_URL3 = "https://apk.tw/home.php?mod=task&do=draw&id=7"

my_data = {'username': 'USERNAME', 'password': 'PASSWORD', 'quickforward': 'yes', 'handlekey': 'ls'}

session_requests = requests.session()

result = session_requests.post(LOGIN_URL, data = my_data)
soup = BeautifulSoup(result.text, 'html.parser')
#print(soup.prettify())
print("Login Success")
result = session_requests.get(REQUEST_URL)
#print(result.status_code)

# REQUEST_URL = "https://apk.tw/" + sys.argv[1] + "&inajax=1&ajaxtarget=my_amupper"
headers = { "Host" : "apk.tw" , "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0" , "Accept" : "*/*" , "Accept-Language" : "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3" , "Accept-Encoding" : "gzip, deflate, br" , "Referer" : "https://apk.tw/forum.php" , "X-Requested-With" : "XMLHttpRequest" , "DNT" : "1" , "Connection" : "keep-alive" , "TE" : "Trailers" }

r = session_requests.get( REQUEST_URL3 , headers=headers)
soup = BeautifulSoup(result.text, 'html.parser')
print(result.status_code)
print("Finish auto sign")

result = session_requests.get(REQUEST_URL2)
soup = BeautifulSoup(result.text, 'html.parser')
print(result.status_code)
#print(soup.prettify())
