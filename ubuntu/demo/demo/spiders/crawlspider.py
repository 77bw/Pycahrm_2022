import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class GumtreeCrawlSpider(CrawlSpider):
    name = 'demo1'
    allowed_domains = ['www.gumtree.com']
    def start_requests(self):
        yield scrapy.Request(
            url='https://world.huanqiu.com/article',
            meta={"playwright": True}
        )
        return super().start_requests()

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//*[contains(@class,'list-item')]/a"), callback='parse_item', follow=False),
    )

    async def parse_item(self, response):
            print(response.text)
            print(response.url)


if __name__ == "__main__":
    process = CrawlerProcess(
        get_project_settings()
    )
    process.crawl(GumtreeCrawlSpider)
    process.start()
