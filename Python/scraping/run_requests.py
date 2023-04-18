#!/usr/bin/python
#-*- coding: UTF-8 -*-

import requests
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
print (strhtml.text)
