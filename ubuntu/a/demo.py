from pathlib import Path

from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess
from scrapy_playwright.page import PageMethod


class ScrollSpider(Spider):
    """
    Scroll down on an infinite-scroll page
    """

    name = "scroll"

    def start_requests(self):
        yield Request(
            url='https://www.hizh.cn/',
            # cookies={
            #     "zycna": "08KRWCMFIm8BAXQVAkMxS6NE",
            #     "Hm_lvt_ba311c77fc37e3e1b1e0e31ea5e8035a": "1650592916,1650939297,1652169515,1652667001",
            #     "acw_tc": "7ce3972416526707943422113e2edf556d8ae80578fa4b8b8df46c2058",
            #     "Hm_lpvt_ba311c77fc37e3e1b1e0e31ea5e8035a": "1652670800"
            # },
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", "//*[@class=\"news-item clink\"][1]"),
                    PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
                    PageMethod("wait_for_selector", "//*[@class=\"news-item clink\"][len(last())+1]"),  # 38 per page
                    PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
                    PageMethod("wait_for_selector", "//*[@class=\"news-item clink\"][len(last())+1]"),
                    PageMethod(
                        "screenshot", path=Path(__file__).parent / "hizh.png", full_page=True
                    ),
                    PageMethod("wait_for_load_state", "networkidle"),
                ],
            },
        )

    def parse(self, response):
        print(response.text)
        print(len(response.xpath('//*[@class=\"news-item clink\"]')))


if __name__ == "__main__":
    process = CrawlerProcess(
        settings={
            "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
            "DOWNLOAD_HANDLERS": {
                "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
                "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            },
            "LOG_LEVEL": "INFO",
        }
    )
    process.crawl(ScrollSpider)
    process.start()