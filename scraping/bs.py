#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.cntour.cn'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
#print(data)

for i in data:
    result = {
        'title': i.get_text(),
        'link': i.get('href'),
        'ID': re.findall('\d+', i.get('href'))
    }
    print(result)