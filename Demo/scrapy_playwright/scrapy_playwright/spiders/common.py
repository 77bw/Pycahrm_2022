import scrapy

class MovieSpider(scrapy.Spider):
    name = 'common'
    allowed_domains = ['antispider1.scrape.center']
    base_url = 'https://antispider1.scrape.center'
    max_page = 10
    custom_settings = {
        'GERAPY_PLAYWRIGHT_PRETEND': True
    }

    def start_requests(self):
        for page in range(1, self.max_page + 1):
            url = f'{self.base_url}/page/{page}'

            yield PlaywrightRequest(url, callback=self.parse_index, priority=10, wait_for='.item')

    def parse_index(self, response):
        print(response.text)
        items = response.css('.item')
        for item in items:
            href = item.css('a::attr(href)').extract_first()
            detail_url = response.urljoin(href)

            yield PlaywrightRequest(detail_url, callback=self.parse_detail, wait_for='.item')

from scrapy import cmdline, Spider
if __name__ == '__main__':
    cmdline.execute("scrapy crawl common".split())