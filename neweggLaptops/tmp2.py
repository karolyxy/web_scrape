import re
from bs4 import BeautifulSoup
import requests
import time
import random
import urllib
import lxml
import csv
import pandas as pd

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100167750%208000&IsNodeId=1&bop=And&ActiveSearchResult=True&order=BESTMATCH&page=1'
response = requests.get(url, headers = headers, timeout = 20).text
print(requests.get(url).status_code)
soup = BeautifulSoup(response, "html.parser")
products = soup.find_all('div', attrs = {'class': "item-info"})

#with open('tmp_newegg_gaming_page1.csv', 'w', encoding='utf-8') as csvfile:
prod_title = products[-6].find('a', attrs = {'class': 'item-title'}).text.strip('\n')
print(prod_title)
if(len(products[-6].find('li', attrs = {'class': 'price-current'}).get_text().strip('\n').split('\n')) == 1):
    print('no value')
else:
    if(products[-6].find('li', attrs = {'class': 'price-current'}).get_text().strip().split('\n')[0] != '|'):
        prod_price = products[-6].find('li', attrs = {'class': 'price-current'}).get_text().strip().split('\n')[0]
        print(prod_price)
    else:
        prod_price = prod_price1 = products[-6].find('li', attrs = {'class': 'price-current'}).get_text().strip().split('\n')[1]
        print(prod_price)
    print(products[-6].find('ul', attrs = {'class': 'item-features'}).get_text().strip('\n').split('\n'))
    if(products[-6].find('ul', attrs = {'class': 'item-features'}).get_text().strip('\n').split('\n')[0].find('Model') == -1):
        prod_model = products[-6].find('ul', attrs = {'class': 'item-features'}).get_text().strip('\n').split('\n')[1]
        print("[1] ", prod_model)
    else:
        prod_model = products[-6].find('ul', attrs = {'class': 'item-features'}).get_text().strip('\n').split('\n')[0]
        print("[0] ", prod_model)



'''
prod_title1 = products[-2].find('a', attrs = {'class': 'item-title'}).text.strip('\n')
print(prod_title1)
if(len(products[-2].find('li', attrs = {'class': 'price-current'}).get_text().strip('\n').split('\n')) == 1):
    print('no value')
else:
    prod_price1 = products[-2].find('li', attrs = {'class': 'price-current'}).get_text().strip().split('\n')[1]
    print(prod_price1)
prod_model1 = products[-2].find('ul', attrs = {'class': 'item-features'}).get_text().strip('\n').split('\n')
print(prod_model1)
'''