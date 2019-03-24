import requests
from bs4 import BeautifulSoup
import time
import sys
import json,os

# 使用方法 python web_scraping.py 辞书名称 网址

page = requests.get(sys.argv[2]).text
soap = BeautifulSoup(page, 'html.parser')
tables = [table for table in soap.find_all('table')]

words = []

for table in tables:
    for tr in table.find_all('tr')[1:]:
        tds = tr.find_all('td')

        tds.remove(tds[2])
        tds = list(map(lambda td: td.string, tds))

        text = ''
        if tds[0]:
            text = tds[0].strip()

        
        kana = ''
        if tds[1]:
            kana = tds[1].strip()
            if text == '':
                text = kana
                kana = ''

        interpre = ''
        if tds[2]:
            interpre = tds[2].strip()
        words.append({
            'text': text,
            'kana': kana,
            'interpres': [{
                'id': 0,
                'text': interpre
            }],
            'media': {
                'type': 'img',
                'content': None
            }
        })

dict = {
    'dict': {
        'id': int(time.time()*1000),
        'name': sys.argv[1]
    },
    'words': words
}

jsonStr = json.dumps(dict, ensure_ascii=False)

with open(sys.argv[1]+'.json', 'w') as file:
    file.write(jsonStr)

print(len(dict['words']))

