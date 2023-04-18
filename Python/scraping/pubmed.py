#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

pmid = '18235848'
url = 'https://pubmed.ncbi.nlm.nih.gov/{}/'.format(pmid)

strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, 'lxml')

#title = soup.select('#full-view-heading > h1') #CSS
title = soup.title.get_text(strip=True)
print(title)
#abstract = soup.select('#enc-abstract > p') #CSS
abstract = soup.p.get_text(strip=True)
print(abstract)
with open('pubmed_ti_ab.txt', 'w') as f2:
    f2.write(title+'\n'+abstract)


