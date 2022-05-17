from scrapy_playwright.page import PageCoroutine
from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess



headers = {
    'authority': 'm.tiktok.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'accept': '*/*',
    'origin': 'https://www.tiktok.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.tiktok.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

class EventSpider(Spider):
    name = "event_b"

    def start_requests(self):
        yield Request(
            url="https://www.tiktok.com/tag/tesla?lang=en",
            headers=headers,
            meta=dict(
                playwright=True,
                playwright_page_coroutines = [
                    PageCoroutine("click", selector = ".tiktok-113bruv-ButtonConfirm.e1ynhqbi10"),
                    PageCoroutine("wait_for_timeout", 3000),
                    PageCoroutine("wait_for_selector", ".tiktok-1qb12g8-DivThreeColumnContainer.e140s4uj2"),
                    PageCoroutine("evaluate", 'setInterval(function () {var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;}, 200);'),
                    PageCoroutine('screenshot', path='test.png', full_page = True)
                ],
            ),callback = self.parse,
        )

    def parse(self, response):
        pass

if __name__ == "__main__":
    process = CrawlerProcess(
        settings={
            "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
            "DOWNLOAD_HANDLERS": {
                # "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
                "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            },
            "LOG_LEVEL": "INFO",
        }
    )
    process.crawl(EventSpider)
    process.start()