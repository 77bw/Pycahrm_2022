import hashlib
import logging
from pathlib import Path
from typing import Generator, Optional
from scrapy.utils.project import get_project_settings
from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from scrapy.http.response import Response


class BooksSpider(Spider):
    """Extract all books, save screenshots."""

    name = "books"
    start_urls = ["http://books.toscrape.com"]

    def parse(self, response: Response, current_page: Optional[int] = None) -> Generator:
        page_count = response.css(".pager .current::text").re_first(r"Page \d+ of (\d+)")
        page_count = int(page_count)
        for page in range(2, page_count + 1):
            yield response.follow(f"/catalogue/page-{page}.html", cb_kwargs={"current_page": page})

        current_page = current_page or 1
        for book in response.css("article.product_pod a"):
            yield response.follow(
                book,
                callback=self.parse_book,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_context": f"page-{current_page}",
                },
            )

    async def parse_book(self, response: Response) -> dict:
        url_sha256 = hashlib.sha256(response.url.encode("utf-8")).hexdigest()
        page = response.meta["playwright_page"]
        await page.screenshot(
            path=Path(__file__).parent / "books" / f"{url_sha256}.png", full_page=True
        )
        await page.close()
        return {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "price": response.css("p.price_color::text").get(),
            "breadcrumbs": response.css(".breadcrumb a::text").getall(),
            "image": f"books/{url_sha256}.png",
        }


if __name__ == "__main__":
    # process = CrawlerProcess(get_project_settings())
    # process.crawl(BooksSpider)
    # logging.getLogger("scrapy.core.engine").setLevel(logging.WARNING)
    # logging.getLogger("scrapy.core.scraper").setLevel(logging.WARNING)
    # process.start()
    import os
    import sys

    __dir__ = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(__dir__)
    sys.path.append(os.path.abspath(os.path.join(__dir__, '../..')))
