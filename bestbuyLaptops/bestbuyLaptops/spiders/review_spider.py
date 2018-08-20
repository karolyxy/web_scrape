from scrapy import Spider, Request
from bestbuyLaptops.items import LaptopReviewItem

class ChromebookReviewSpider(Spider):
    name = "chromebook_review"
    allowed_urls = ['https://www.bestbuy.com/']
    start_urls = ['https://www.bestbuy.com/site/all-laptops/chromebooks/pcmcat244900050010.c?id=pcmcat244900050010']

    custom_settings = {
        'ITEM_PIPELINES': {'bestbuyLaptops.pipelines.ChromebookReviewPipeline': 200}
    }

    def parse(self, response):
        # Find the total number of pages in the result so that we can decide how many urls to scrape next
        # List comprehension to construct all thxe urls
        result_urls = ['https://www.bestbuy.com/site/all-laptops/pc-laptops/pcmcat247400050000.c?cp={}&id=pcmcat247400050000'.format(x) for x in range(1, 5)]

        print("all product page")

        for url in result_urls:
            yield Request(url = url, callback = self.parse_result_page)


    def parse_result_page(self, response):

        detail_urls = response.xpath('//div[@class="sku-title"]/h4/a/@href').extract()

        # Yield the requests to the details pages,
        # using parse_detail_page function to parse the response.
        for url in detail_urls:
            yield Request(url=url, callback=self.parse_detail_page)


    def parse_detail_page(self, response):

        review_page = response.xpath('//div[@class="see-all-reviews-button-container"]/a/@href').extract_first()

        print("review: ", review_page)

        yield Request(url = review_page, callback=self.parse_review_page)


    def parse_review_page(self, response):

        reviews = response.xpath('//li[@class="review-item"]')
        prod_title = response.xpath('//a[@data-track="Product Description"]/text()').extract_first()

        for review in reviews:

            print('review')

            try:
                helpful = review.xpath('.//button[@data-track="Helpful"]/text()').extract()[1]
                num_helpful = int(helpful)
            except IndexError:
                helpful = ""
            try:
                unhelpful = review.xpath('.//button[@data-track="Unhelpful"]/text()').extract()[1]
                num_unhelpful = int(unhelpful)
            except IndexError:
                unhelpful = 0

            if num_helpful>0 and num_helpful>num_unhelpful:
                user = review.xpath('.//div[@class="undefined ugc-author v-fw-medium body-copy-lg"]/text()').extract_first()
                rating = review.xpath('.//span[@class="c-review-average"]/text()').extract_first()
                review_title = review.xpath('.//h3[@class="ugc-review-title c-section-title heading-5 v-fw-medium  "]/text()').extract_first()
                text = review.xpath('.//p[@class="pre-white-space"]/text()').extract_first()

                item = LaptopReviewItem()
                item['user'] = user
                item['rating'] = rating
                item['review_title'] = review_title
                item['text'] = text
                item['helpful'] = helpful
                item['unhelpful'] = unhelpful
                item['prod_title'] = prod_title

                yield item

        total_review = int(''.join(response.xpath('//span[@class="c-total-reviews"]/text()').extract()[1].split(',')))
        num_pages = total_review // 20 + 1
        following_urls = [response.url + '?page={}'.format(x) for x in range(2, num_pages + 1)]

        for url in following_urls:
            yield Request(url=url, callback=self.parse_following_review_page)


    def parse_following_review_page(self, response):

        reviews = response.xpath('//li[@class="review-item"]')
        prod_title = response.xpath('//a[@data-track="Product Description"]/text()').extract_first()

        for review in reviews:
            print('following reviews')

            try:
                helpful = review.xpath('.//button[@data-track="Helpful"]/text()').extract()[1]
                num_helpful = int(helpful)
            except IndexError:
                helpful = ""
            try:
                unhelpful = review.xpath('.//button[@data-track="Unhelpful"]/text()').extract()[1]
                num_unhelpful = int(unhelpful)
            except IndexError:
                unhelpful = 0

            if num_helpful > 0 and num_helpful > num_unhelpful:
                user = review.xpath(
                    './/div[@class="undefined ugc-author v-fw-medium body-copy-lg"]/text()').extract_first()
                rating = review.xpath('.//span[@class="c-review-average"]/text()').extract_first()
                review_title = review.xpath(
                    './/h3[@class="ugc-review-title c-section-title heading-5 v-fw-medium  "]/text()').extract_first()
                text = review.xpath('.//p[@class="pre-white-space"]/text()').extract_first()

                item = LaptopReviewItem()
                item['user'] = user
                item['rating'] = rating
                item['review_title'] = review_title
                item['text'] = text
                item['helpful'] = helpful
                item['unhelpful'] = unhelpful
                item['prod_title'] = prod_title

                yield item


class BusinessLaptopReviewSpider(Spider):
    name = "businessLaptop_review"
    allowed_urls = ['https://www.bestbuy.com/']
    start_urls = ['https://www.bestbuy.com/site/all-laptops/business-laptops/pcmcat376300050005.c?id=pcmcat376300050005']

    custom_settings = {
        'ITEM_PIPELINES': {'bestbuyLaptops.pipelines.BusinessLaptopReviewPipeline': 200}
    }

    def parse(self, response):
        # Find the total number of pages in the result so that we can decide how many urls to scrape next
        # List comprehension to construct all thxe urls
        result_urls = ['https://www.bestbuy.com/site/all-laptops/business-laptops/pcmcat376300050005.c?cp={}&id=pcmcat376300050005'.format(x) for x in range(1, 5)]

        print("all product page")

        for url in result_urls:
            yield Request(url=url, callback=self.parse_result_page)

    def parse_result_page(self, response):

        detail_urls = response.xpath('//div[@class="sku-title"]/h4/a/@href').extract()

        print("result page")

        # Yield the requests to the details pages,
        # using parse_detail_page function to parse the response.
        for url in detail_urls:
            yield Request(url=url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):

        first_reviews = response.xpath('//li[@class="review-item"]')

        if len(first_reviews) == 0:
            # If the product does not have any reviews, we just return.
            return
        elif len(first_reviews) < 8:
            # If there are less than 8 reviews, we just scrape/yield all of them and call it a day.
            # Extract each field from the review tag
            prod_title = response.xpath('//h1[@class="heading-5 v-fw-regular"]/text()').extract_first()
            for review in first_reviews:
                user = review.xpath('.//div[@class="undefined ugc-author v-fw-medium body-copy-lg"]/text()').extract_first()
                rating = review.xpath('.//span[@class="c-review-average"]/text()').extract_first()
                review_title = review.xpath('.//h3[@class="ugc-review-title c-section-title heading-5 v-fw-medium  "]/text()').extract_first()
                text = review.xpath('.//p[@class="pre-white-space"]/text()').extract_first()
                try:
                    helpful = review.xpath('.//button[@data-track="Helpful"]/text()').extract()[1]
                except IndexError:
                    helpful = ""
                try:
                    unhelpful = review.xpath('.//button[@data-track="Unhelpful"]/text()').extract()[1]
                except IndexError:
                    unhelpful = ""

                item = LaptopReviewItem()
                item['user'] = user
                item['rating'] = rating
                item['review_title'] = review_title
                item['text'] = text
                item['helpful'] = helpful
                item['unhelpful'] = unhelpful
                item['prod_title'] = prod_title

                yield item
        else:
            review_page = response.xpath('//div[@class="see-all-reviews-button-container"]/a/@href').extract_first()

            #print("review: ", review_page)

            yield Request(url=review_page, callback=self.parse_review_page)

    def parse_review_page(self, response):

        reviews = response.xpath('//li[@class="review-item"]')
        prod_title = response.xpath('//a[@data-track="Product Description"]/text()').extract_first()

        for review in reviews:

            #print('review')
            user = review.xpath('.//div[@class="undefined ugc-author v-fw-medium body-copy-lg"]/text()').extract_first()
            rating = review.xpath('.//span[@class="c-review-average"]/text()').extract_first()
            review_title = review.xpath('.//h3[@class="ugc-review-title c-section-title heading-5 v-fw-medium  "]/text()').extract_first()
            text = review.xpath('.//p[@class="pre-white-space"]/text()').extract_first()

            try:
                helpful = review.xpath('.//button[@data-track="Helpful"]/text()').extract()[1]
                num_helpful = int(helpful)
            except IndexError:
                helpful = ""
            try:
                unhelpful = review.xpath('.//button[@data-track="Unhelpful"]/text()').extract()[1]
                num_unhelpful = int(unhelpful)
            except IndexError:
                unhelpful = 0

            item = LaptopReviewItem()
            item['user'] = user
            item['rating'] = rating
            item['review_title'] = review_title
            item['text'] = text
            item['helpful'] = helpful
            item['unhelpful'] = unhelpful
            item['prod_title'] = prod_title

            yield item

        total_review = int(''.join(response.xpath('//span[@class="c-total-reviews"]/text()').extract()[1].split(',')))
        num_pages = total_review // 20 + 1
        following_urls = [response.url + '?page={}'.format(x) for x in range(2, num_pages + 1)]

        for url in following_urls:
            yield Request(url=url, callback=self.parse_following_review_page)

    def parse_following_review_page(self, response):

        reviews = response.xpath('//li[@class="review-item"]')
        prod_title = response.xpath('//a[@data-track="Product Description"]/text()').extract_first()

        for review in reviews:

            # print('review')
            user = review.xpath('.//div[@class="undefined ugc-author v-fw-medium body-copy-lg"]/text()').extract_first()
            rating = review.xpath('.//span[@class="c-review-average"]/text()').extract_first()
            review_title = review.xpath(
                './/h3[@class="ugc-review-title c-section-title heading-5 v-fw-medium  "]/text()').extract_first()
            text = review.xpath('.//p[@class="pre-white-space"]/text()').extract_first()

            try:
                helpful = review.xpath('.//button[@data-track="Helpful"]/text()').extract()[1]
                num_helpful = int(helpful)
            except IndexError:
                helpful = ""
            try:
                unhelpful = review.xpath('.//button[@data-track="Unhelpful"]/text()').extract()[1]
                num_unhelpful = int(unhelpful)
            except IndexError:
                unhelpful = 0

            item = LaptopReviewItem()
            item['user'] = user
            item['rating'] = rating
            item['review_title'] = review_title
            item['text'] = text
            item['helpful'] = helpful
            item['unhelpful'] = unhelpful
            item['prod_title'] = prod_title

            yield item



class GamingLaptopReviewSpider(Spider):
    name = "gamingLaptop_review"
    allowed_urls = ['https://www.bestbuy.com/']
    start_urls = ['https://www.bestbuy.com/site/all-laptops/gaming-laptops/pcmcat287600050003.c?id=pcmcat287600050003']

    custom_settings = {
        'ITEM_PIPELINES': {'bestbuyLaptops.pipelines.GamingLaptopReviewPipeline': 200}
    }

    def parse(self, response):
        # Find the total number of pages in the result so that we can decide how many urls to scrape next
        # List comprehension to construct all thxe urls
        result_urls = ['https://www.bestbuy.com/site/all-laptops/gaming-laptops/pcmcat287600050003.c?cp={}&id=pcmcat287600050003'.format(x) for x in range(1, 7)]

        print("all product page")

        for url in result_urls:
            yield Request(url=url, callback=self.parse_result_page)

    def parse_result_page(self, response):

        detail_urls = response.xpath('//div[@class="sku-title"]/h4/a/@href').extract()

        # Yield the requests to the details pages,
        # using parse_detail_page function to parse the response.
        for url in detail_urls:
            yield Request(url=url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):

        first_reviews = response.xpath('//li[@class="review-item"]')
        #prod_title = response.xpath('//a[@data-track="Product Description"]/text()').extract_first()
        if len(first_reviews) == 0:
            # If the product does not have any reviews, we just return.
            return
        elif len(first_reviews) < 8:
            # If there are less than 8 reviews, we just scrape/yield all of them and call it a day.
            # Extract each field from the review tag
            prod_title = response.xpath('//h1[@class="heading-5 v-fw-regular"]/text()').extract_first()
            for review in first_reviews:
                user = review.xpath('.//div[@class="undefined ugc-author v-fw-medium body-copy-lg"]/text()').extract_first()
                rating = review.xpath('.//span[@class="c-review-average"]/text()').extract_first()
                review_title = review.xpath('.//h3[@class="ugc-review-title c-section-title heading-5 v-fw-medium  "]/text()').extract_first()
                text = review.xpath('.//p[@class="pre-white-space"]/text()').extract_first()
                try:
                    helpful = review.xpath('.//button[@data-track="Helpful"]/text()').extract()[1]
                except IndexError:
                    helpful = ""
                try:
                    unhelpful = review.xpath('.//button[@data-track="Unhelpful"]/text()').extract()[1]
                except IndexError:
                    unhelpful = ""

                item = LaptopReviewItem()
                item['user'] = user
                item['rating'] = rating
                item['review_title'] = review_title
                item['text'] = text
                item['helpful'] = helpful
                item['unhelpful'] = unhelpful
                item['prod_title'] = prod_title

                yield item
        else:
            review_page = response.xpath('//div[@class="see-all-reviews-button-container"]/a/@href').extract_first()

            #print("review: ", review_page)

            yield Request(url=review_page, callback=self.parse_review_page)

    def parse_review_page(self, response):

        reviews = response.xpath('//li[@class="review-item"]')
        prod_title = response.xpath('//a[@data-track="Product Description"]/text()').extract_first()

        for review in reviews:

            print('review')

            try:
                helpful = review.xpath('.//button[@data-track="Helpful"]/text()').extract()[1]
                num_helpful = int(helpful)
            except IndexError:
                helpful = ""
            try:
                unhelpful = review.xpath('.//button[@data-track="Unhelpful"]/text()').extract()[1]
                num_unhelpful = int(unhelpful)
            except IndexError:
                unhelpful = 0

            if num_helpful > 0 and num_helpful > num_unhelpful:
                user = review.xpath(
                    './/div[@class="undefined ugc-author v-fw-medium body-copy-lg"]/text()').extract_first()
                rating = review.xpath('.//span[@class="c-review-average"]/text()').extract_first()
                review_title = review.xpath(
                    './/h3[@class="ugc-review-title c-section-title heading-5 v-fw-medium  "]/text()').extract_first()
                text = review.xpath('.//p[@class="pre-white-space"]/text()').extract_first()

                item = LaptopReviewItem()
                item['user'] = user
                item['rating'] = rating
                item['review_title'] = review_title
                item['text'] = text
                item['helpful'] = helpful
                item['unhelpful'] = unhelpful
                item['prod_title'] = prod_title

                yield item

        total_review = int(''.join(response.xpath('//span[@class="c-total-reviews"]/text()').extract()[1].split(',')))
        num_pages = total_review // 20 + 1
        following_urls = [response.url + '?page={}'.format(x) for x in range(2, num_pages + 1)]

        for url in following_urls:
            yield Request(url=url, callback=self.parse_following_review_page)

    def parse_following_review_page(self, response):

        reviews = response.xpath('//li[@class="review-item"]')
        prod_title = response.xpath('//a[@data-track="Product Description"]/text()').extract_first()

        for review in reviews:
            print('following reviews')

            try:
                helpful = review.xpath('.//button[@data-track="Helpful"]/text()').extract()[1]
                num_helpful = int(helpful)
            except IndexError:
                helpful = ""
            try:
                unhelpful = review.xpath('.//button[@data-track="Unhelpful"]/text()').extract()[1]
                num_unhelpful = int(unhelpful)
            except IndexError:
                unhelpful = 0

            if num_helpful > 0 and num_helpful > num_unhelpful:
                user = review.xpath(
                    './/div[@class="undefined ugc-author v-fw-medium body-copy-lg"]/text()').extract_first()
                rating = review.xpath('.//span[@class="c-review-average"]/text()').extract_first()
                review_title = review.xpath(
                    './/h3[@class="ugc-review-title c-section-title heading-5 v-fw-medium  "]/text()').extract_first()
                text = review.xpath('.//p[@class="pre-white-space"]/text()').extract_first()

                item = LaptopReviewItem()
                item['user'] = user
                item['rating'] = rating
                item['review_title'] = review_title
                item['text'] = text
                item['helpful'] = helpful
                item['unhelpful'] = unhelpful
                item['prod_title'] = prod_title

                yield item