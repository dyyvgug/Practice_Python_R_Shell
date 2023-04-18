#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import re
import json

url = 'http://www.cntour.cn'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
tour_file = open("tour_file.txt", 'a', encoding='utf-8')
#print(data)
#print(type(data))

for i in data:
    result = {
        'title': i.get_text(),
        'link': i.get('href'),
        'ID': re.findall('\d+', i.get('href'))
    }
    print(result)
    tour_file.write(json.dumps(result, ensure_ascii=False, indent=3))
