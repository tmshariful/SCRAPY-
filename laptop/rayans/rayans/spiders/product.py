import scrapy

class startechSpider(scrapy.Spider):
    name = "ryans"
    dont_filter = True
    start_urls = ["https://www.ryanscomputers.com/category/laptop-all-laptop?page=1&limit=90&query="]

    def parse(self,response):
        for product in response.css('div.product-content-info'):
            yield {
                'name': product.css('a.product-title-grid::text').get(),
                'price': product.css('span.price::text').get().lstrip(),
                'link': product.css('a.product-title-grid').attrib['href'],
                 }

        x = response.css("div.pages a::text").getall()
        value = int((x[-2])) + 1
        for a in range(2,value):
            yield (scrapy.Request(f'https://www.ryanscomputers.com/category/laptop-all-laptop?page=' + str(a) +'&limit=90&query=', callback= self.parse))

