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
url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100167732%208000&IsNodeId=1&bop=And&ActiveSearchResult=True&order=BESTMATCH&page=1'

response = requests.get(url, headers = headers, timeout = 20).text
print(requests.get(url).status_code)
soup = BeautifulSoup(response, "html.parser")
products = soup.find_all('div', attrs = {'class': "item-info"})

with open('tmp_newegg_gaming_page1.csv', 'w', encoding='utf-8') as csvfile:
    prod_writer = csv.writer(csvfile)
    prod_dict = {}
    for product in products:
        prod_title = product.find('a', attrs = {'class': 'item-title'}).text.strip('\n')
        #print(prod_title)
        if(len(product.find('li', attrs = {'class': 'price-current'}).get_text().strip('\n').split('\n')) == 1):
            print('no value')
        else:
            prod_price = product.find('li', attrs = {'class': 'price-current'}).get_text().strip('\n').split('\n')[1].strip()
            #print(prod_price)
        #print(prod_price)
        prod_model = product.find('ul', attrs = {'class': 'item-features'}).get_text().strip('\n').split('\n')[1]
        #print(prod_model)
        prod_dict['title'] = prod_title
        prod_dict['model'] = prod_model
        prod_dict['price'] = prod_price
        time.sleep(random.randint(1, 3))
        prod_writer.writerow(prod_dict.values())
