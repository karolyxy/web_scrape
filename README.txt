name: Karol Yuan
partner: N/A
email: karolyxy@gmail.com
project name: Web Scrapping Project 

This submission includes three parts of work:
1. ~/neweggLaptops/:
	- web scrapping by using BeautifulSoup and Re
2. ~/bestbuyLaptops/:
	- web scrapping by implementing Scrapy and Xpath
3. ~/newegg_bestbuy/:
	- general processing by R of csv files that produced by web scrapping such as:
		- cleaning out invalid characters and unnecessary information
		- adjust columns to a more acceptable order than the original ones
		- (R automatic) label each row with indicies
4. ~/laptop_shopper/:
	-  Using R and shinydashboard to present all clean data
5. all csv files after cleaning
6. README.txt: index of files

How to run: Navigate to the directory that contains all of these files using Terminal/Command Line.
- To get the data about newegg laptops, type following on terminal/command line:
	- chromebook: python newegg_chromebook.py
	- business laptops: python newegg_businessLaptop.py
	- gaming laptops: python newegg_gamingLaptop.py
- To get the data about bestbuy laptops, type following on terminal/command line:
	- chromebook: scrapy crawl chromebook_spider
	- business laptops: scrapy crawl businesslaptop_spider
	- gaming laptops: scrapy crawl gaminglaptop_spider
- To get the data about consumers' reviews corresponding to the product scraped above:
	- chromebook: scrapy crawl chromebook_review
	- business laptops: scrapy crawl businessLaptop_review
	- gaming laptops: scrapy crawl gamingLaptop_review
