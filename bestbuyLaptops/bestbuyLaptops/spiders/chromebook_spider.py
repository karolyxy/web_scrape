from scrapy import Spider
from bestbuyLaptops.items import BestbuylaptopsItem

class ChromebookSpider(Spider):
    name = 'chromebook_spider'
    allowed_urls = ['https://www.bestbuy.com/']
    start_urls = ['https://www.bestbuy.com/site/all-laptops/chromebooks/pcmcat244900050010.c?cp={}&id=pcmcat244900050010'.format(x) for x in range(1, 5)]
    custom_settings = {
        'ITEM_PIPELINES':{'bestbuyLaptops.pipelines.ChromebookWriteItemPipeline': 200}
    }

    def parse(self, response):
        # List comprehension to construct all the urls
        #print("Start Working")

        products = response.xpath('//li[@class="sku-item"]')
        #print(products)
        for product in products:
            title = product.xpath('.//div[@class="sku-title"]/h4/a/text()').extract()
            model = product.xpath('.//div[@class="sku-model"]/div[1]/span[2]/text()').extract()
            price = product.xpath('.//div[@class="priceView-hero-price priceView-purchase-price"]/span/text()').extract()

           # print(title)
           # print(model)
           # print(price)
            item = BestbuylaptopsItem()
            item['price'] = price
            item['model'] = model
            item['title'] = title
            yield item

        print("Finish Working")

class GaminglaptopSpider(Spider):
    name = "gaminglaptop_spider"

    allowed_urls = ['https://www.bestbuy.com/']
    start_urls = ['https://www.bestbuy.com/site/all-laptops/gaming-laptops/pcmcat287600050003.c?cp={}&id=pcmcat287600050003'.format(x) for x in range(1, 7)]
    custom_settings = {
        'ITEM_PIPELINES': {'bestbuyLaptops.pipelines.GamingLaptopWriteItemPipeline': 200}
    }

    def parse(self, response):
        # List comprehension to construct all the urls
        #print("Start Working")

        products = response.xpath('//li[@class="sku-item"]')
        #print(products)
        for product in products:
            title = product.xpath('.//div[@class="sku-title"]/h4/a/text()').extract()
            model = product.xpath('.//div[@class="sku-model"]/div[1]/span[2]/text()').extract()
            price = product.xpath('.//div[@class="priceView-hero-price priceView-purchase-price"]/span/text()').extract()

           # print(title)
           # print(model)
           # print(price)
            item = BestbuylaptopsItem()
            item['price'] = price
            item['model'] = model
            item['title'] = title
            yield item



class BusinessLaptopSpider(Spider):
    name = "businesslaptop_spider"

    allowed_urls = ['https://www.bestbuy.com/']
    start_urls = ['https://www.bestbuy.com/site/all-laptops/business-laptops/pcmcat376300050005.c?cp={}&id=pcmcat376300050005'.format(x) for x in range(1, 5)]
    custom_settings = {
        'ITEM_PIPELINES': {'bestbuyLaptops.pipelines.BusinessLaptopWriteItemPipeline': 200}
    }

    def parse(self, response):
        # List comprehension to construct all the urls
        # print("Start Working")

        products = response.xpath('//li[@class="sku-item"]')
        # print(products)
        for product in products:
            title = product.xpath('.//div[@class="sku-title"]/h4/a/text()').extract()
            model = product.xpath('.//div[@class="sku-model"]/div[1]/span[2]/text()').extract()
            price = product.xpath(
                './/div[@class="priceView-hero-price priceView-purchase-price"]/span/text()').extract()

            # print(title)
            # print(model)
            # print(price)
            item = BestbuylaptopsItem()
            item['price'] = price
            item['model'] = model
            item['title'] = title
            yield item