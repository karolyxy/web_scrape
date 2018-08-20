import re
from bs4 import BeautifulSoup
import requests
import time
import random
import csv


headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

# Chromebook page product info: newegg page 1-3
urls = ["https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100167750%208000&IsNodeId=1&page={}".format(str(i)) for i in range(1, 4)]


def scrape_single_page(products, csvwriter):
    for product in products:
        dic = {}
        # print("product title length: ", len(prod_title))
        if (len(product.find('li', attrs={'class': 'price-current'}).get_text().strip('\n').split('\n')) == 1):
            continue
        else:
            if (product.find('li', attrs={'class': 'price-current'}).get_text().strip().split('\n')[0] != '|'):
                prod_price = product.find('li', attrs={'class': 'price-current'}).get_text().strip().split('\n')[0].strip()
                # print(prod_price)
            else:
                prod_price = product.find('li', attrs={'class': 'price-current'}).get_text().strip().split('\n')[1].strip()
                # print(prod_price)
            prod_title = product.find('a', attrs = {'class': 'item-title'}).get_text()
        #print('price: ',len(prod_price))
            if (product.find('ul', attrs={'class': 'item-features'}).get_text().strip('\n').split('\n')[0].find('Model') == -1):
                prod_model = product.find('ul', attrs={'class': 'item-features'}).get_text().strip('\n').split('\n')[1]
                print("[1] ", prod_model)
            else:
                prod_model = product.find('ul', attrs={'class': 'item-features'}).get_text().strip('\n').split('\n')[0]
                print("[0] ", prod_model)

        #print('model: ', len(prod_model))
            dic['title'] = prod_title
        #print("aaaa")
        #print('bbbb')
            dic['model'] = prod_model
            dic['price'] = prod_price
        #print("ccccc")
        csvwriter.writerow(dic.values())
        #print("csv writing")

with open('newegg_chromebook.csv', 'w', encoding='utf-8') as csvfile: # set encoding, otherwise 'gbk' as default
    product_writer = csv.writer(csvfile)
    for index, url in enumerate(urls):
        response = requests.get(url, headers = headers, timeout = 20).text
        soup = BeautifulSoup(response, 'html.parser')
        print(requests.get(url).status_code) # right status code: 200, 403 for detected web scrapper
        products = soup.find_all('div', attrs={'class': 'item-info'})
        scrape_single_page(products, product_writer)
        time.sleep(random.randint(1, 3))
        print('Finished page '+str(index+1))


# first producL: Lenovo Flex 11 Chormebook
'''
first_prod = products[0]
first_prod_title = first_prod.find('a', attrs = {'class': 'item-title'}).text
print(first_prod_title)
first_prod_price = first_prod.find('li', attrs = {'class': 'price-current'}).get_text()
print(first_prod_price.strip().split('\n')[1].strip())
first_prod_model = first_prod.find('ul', attrs = {'class': 'item-features'}).get_text()
print(first_prod_model.strip().split('\n')[1])
'''
