#!/usr/bin/python
#coding:utf-8

import urllib2
import re
keyword = re.compile('disease')
pmids = ['18235848','22607149','22405002','21630672']
for pmid in pmids:
	url = 'http://www.ncbi.nlm.nih.gov/pubmed?term={}'.format(pmid)
	handler = urllib2.urlopen(url)
	html = handler.read()
	title_regexp = re.compile('<title>(.{5,400})  - PubMed')
	title_text = title_regexp.search(html)
	abstract_regexp = re.compile('<h3>Abstract</h3><div class=""><p>(.{20,5000})</p></div>')
	abstract_text = abstract_regexp.search(html)
	#print 'TITLE:',title_text.group(1)
	#print 'ABSTRACT:',abstract_text.group(1)
	abstract = abstract_text.group(1)
	#word = keyword.search(abstract,re.IGNORECASE)    #only first 
	words = keyword.finditer(abstract)
	if words:
		print 'TITLE:',title_text.group(1)
		for word in words:
			print word.group(),word.start(),word.end()
