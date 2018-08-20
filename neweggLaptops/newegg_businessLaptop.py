import re
from bs4 import BeautifulSoup
import requests
import time
import random
import csv

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

urls = ["https://www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100006740%20600337746%20600566284%20600364421%20600004958"
        "%20600472974%20600004970%208000&IsNodeId=1&OEMMark=N&bop=And&order=BESTMATCH&page={}".format(str(i)) for i in range(1, 9)]

def scrape_single_page(products, csvwriter):
    dic = {}

    for product in products:
        if (len(product.find('li', attrs={'class': 'price-current'}).get_text().strip('\n').split('\n')) == 1):
            print(product.find('li', attrs={'class': 'price-current'}).get_text().strip('\n').split('\n')[1].strip(), ": no price")
            continue
        else:
            if (product.find('li', attrs={'class': 'price-current'}).get_text().strip().split('\n')[0] != '|'):
                prod_price = product.find('li', attrs={'class': 'price-current'}).get_text().strip().split('\n')[0].strip()
                #print(prod_price)
            else:
                prod_price = product.find('li', attrs={'class': 'price-current'}).get_text().strip().split('\n')[1].strip()
                #print(prod_price)
            prod_title = product.find('a', attrs={'class': 'item-title'}).get_text()
            prod_model = product.find('ul', attrs={'class': 'item-features'}).get_text().strip('\n').split('\n')[1]
            dic['title'] = prod_title
            dic['model'] = prod_model
            dic['price'] = prod_price

            csvwriter.writerow(dic.values())


with open('newegg_businessLaptop.csv', 'w', encoding='utf-8') as csvfile:
    product_writer = csv.writer(csvfile)
    for index, url in enumerate(urls):
        response = requests.get(url, headers=headers, timeout=20).text
        soup = BeautifulSoup(response, 'html.parser')
        print(requests.get(url).status_code)  # right status code: 200, 403 for detected web scrapper
        products = soup.find_all('div', attrs={'class': 'item-info'})
        scrape_single_page(products, product_writer)
        time.sleep(random.randint(1, 3))
        print('Finished page ' + str(index + 1))