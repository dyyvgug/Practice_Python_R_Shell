#!/usr/bin/python
import requests
import re
import json

def get_one_page(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    response = requests.get(url, headers=head)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile(
        'class="name">.*?<a.*?>(.*?)</a>.*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        print(item)
        yield {
            'title': item[0],
            'star': item[1].strip(),
            'time': item[2]
        }

def write_to_file(content):
    with open('flv_result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False, indent=3))

def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__ == '__main__':
    main()
