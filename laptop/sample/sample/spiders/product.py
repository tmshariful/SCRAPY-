import scrapy

class startechSpider(scrapy.Spider):
    name = "laptop"
    dont_filter = True
    start_urls = ["https://www.startech.com.bd/laptop-notebook/laptop?limit=48&page=1"]

    def parse(self,response):
        for products in response.css('div.p-item'):
            yield {
                'name': products.css('h4.p-item-name a::text').get(),
                'price': products.css('div.p-item-price span::text').get().replace('৳',''),
                'link': products.css('h4.p-item-name a').attrib['href'],
                 }

        x = response.css("ul.pagination a::text").getall()
        value = int((x[-2]))
        for a in range(2,value):
            yield (scrapy.Request(f'https://www.startech.com.bd/laptop-notebook/laptop?limit=48&page=' + str(a), callback= self.parse))

