import re
from bs4 import BeautifulSoup
import requests
import time
import random
import csv

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

#urls = ["https://www.bestbuy.com/site/all-laptops/chromebooks/pcmcat244900050010.c?cp={}&id=pcmcat244900050010".format(str(i)) for i in range(1, 5)]

url = 'https://www.bestbuy.com/site/all-laptops/chromebooks/pcmcat244900050010.c?cp=1&id=pcmcat244900050010'

response = requests.get(url, headers = headers, timeout = 20).text
print(requests.get(url).status_code)
soup = BeautifulSoup(response, "html.parser")
products = soup.find_all('div', attrs={'class': 'sku-title'})

prod_title = products[1].find('h4', attrs={'class': 'sku-header'}).text
print(prod_title)
print(type(products[1].find('div', attrs={'class': 'sku-list-item-price'})))
# <div class="priceView-hero-price priceView-purchase-price"><span aria-label="Your price for this item is $199.00">$<!-- -->199.00</span></div>
print(prod_price)