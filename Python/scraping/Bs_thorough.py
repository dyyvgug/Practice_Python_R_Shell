from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, 'lxml')

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.find_all('b'))
print(soup.find_all(["a", "b"]))
print(soup.get_text())
print(soup.find_all("title"))
title = str(soup.find_all("title"))
print(soup.p.get_text())
print(soup.title.get_text())
with open('exp.txt', 'a') as f:
    f.write(soup.title.get_text()+title+'\n')
    f.write(soup.get_text())

markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)

print(soup.get_text('|', strip=True))
print(soup.i.get_text())

