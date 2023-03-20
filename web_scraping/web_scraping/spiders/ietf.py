import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['https://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        return {
            "title": response.xpath("//span[@class='title']/text()").get(),
            "text": response.xpath("//div[@class = 'text']//text()").getall(),
            "author": response.xpath("//span[@class='author-name']/text()").get(),
            "meta_author" : response.xpath("//meta[@name = 'DC.Creator']/@content").get(),
        }
