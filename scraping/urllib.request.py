#!/usr/bin/python
#-*- coding: UTF-8 -*-


import urllib.request


url = "http://www.baidu.com"
response1 = urllib.request.urlopen(url)
print ("first method")
print (response1.getcode)
print (len(response1.read()))
