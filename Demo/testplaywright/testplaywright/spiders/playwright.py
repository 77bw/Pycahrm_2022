import scrapy

class AwesomeSpider(scrapy.Spider):
    name = "playwright"

    def start_requests(self):
        # GET request
        yield scrapy.Request('https://spa6.scrape.center/', meta={"playwright": True})
        # POST reques

    def parse(self, response):
        print(response.text)
        print(response.url)
        # 'response' contains the page as seen by the browser
        # yield {"url": response.url}

# import scrapy
#
# class AwesomeSpiderWithPage(scrapy.Spider):
#     name = "playwright"
#
#     def start_requests(self):
#         yield scrapy.Request(
#             url="https://example.org",
#             meta={"playwright": True, "playwright_include_page": True},
#             errback=self.errback,
#         )
#
#     async def parse(self, response):
#         page = response.meta["playwright_page"]
#         title = await page.title()  # "Example Domain"
#         await page.close()
#         return {"title": title}
#
#     async def errback(self, failure):
#         page = failure.request.meta["playwright_page"]
#         await page.close()