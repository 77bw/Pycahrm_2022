import asyncio

import scrapy.http
from playwright.async_api import async_playwright
from  scrapy.http import HtmlResponse
from playwright.sync_api import sync_playwright

class PlayerightMiddleware(object):
    async def main(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto(self.url)
            await page.wait_for_load_state('networkidle')
            data = await page.content()
            await browser.close()
            return data

    def process_reguest(self,request,spider):
        self.url = request.url
        # self.url = 'https://spa6.scrape.center/'
        # _data = asyncio.run(self.main())
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.url)
            page.wait_for_load_state('networkidle')
            html = page.content()
            browser.close()
        # print(_data)
        # url='https://spa6.scrape.center/'
        response = scrapy.http.Response(url=self.url,body=html,encoding='utf-8',request=request)
        return response

if __name__ == '__main__':
    middleware=PlayerightMiddleware()
    res=middleware.process_reguest()
    print(res)
    print(res.encoding)
    print(res.text)