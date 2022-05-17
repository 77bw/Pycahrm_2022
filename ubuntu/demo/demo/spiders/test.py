from scrapy.utils.project import get_project_settings
import scrapy
from scrapy_playwright.page import PageCoroutine,PageMethod
from scrapy.crawler import CrawlerProcess


class DoorSpider(scrapy.Spider):
    name = 'demo'
    # start_urls = 'https://spa6.scrape.center/'
    start_urls = 'https://www.hizh.cn/'

    def start_requests(self):
        # yield scrapy.Request(
        #     url=self.start_urls,
        #     callback=self.parse,
        #     meta=dict(
        #         playwright=True,
        #         playwright_include_page=True,
        #         playwright_page_coroutines=[
        #             PageCoroutine("wait_for_load_state", "load")
        #
        #         ]
        #     )
        # )

        # yield scrapy.Request(self.start_urls, meta={'playwright': True,   #开启playwright
        #                                      "playwright_include_page": True,  #在回调中接收 Page 对象
        #                                      'playwright_page_methods': [    #设置page的有关操作
        # PageMethod("wait_for_load_state", "networkidle") , #获取源码必带的条件,
        #
        #                                      ]
        #                                             })
        #
        yield scrapy.Request(self.start_urls, meta={'playwright': True,   #开启playwright
                                             "playwright_include_page": True,  #在回调中接收 Page 对象
                                                     "playwright_page_methods" : [
                                                         # PageMethod("wait_for_selector", "//*[@class=\"news-item clink\"]"),
                                                         PageMethod("evaluate",
                                                                    "window.scrollTo(0,document.documentElement.scrollHeight)"),
                                                         # PageMethod("wait_for_selector", "//*[@class=\"news-item clink\"][121]"),
                                                     PageMethod("wait_for_load_state", "networkidle") ]
                                                    })



    async def parse(self, response):
        page = response.meta["playwright_page"]
        page_methods = response.meta["playwright_page_methods"]
        page.close()
        for i in range(3):
            yield scrapy.Request(url = self.start_urls ,meta = {"page_methods":page_methods,"page":page} ,callback = self.parse1)

    def parse1(self, response):
        page = response.meta["page"]
        page.close()
        print(response.text)

if __name__ == "__main__":
    process = CrawlerProcess(
        get_project_settings()
    )
    process.crawl(DoorSpider)
    process.start()


