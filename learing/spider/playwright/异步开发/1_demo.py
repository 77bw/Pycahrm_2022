#async_playwright 方法，而不再是 sync_playwright 方法。写法上添加了 async/await 关键字的使用，最后的运行效果是一样的。

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('https://www.baidu.com')
            await page.screenshot(path=f'screenshot-{browser_type.name}.png')
            print(await page.title())
            await browser.close()

asyncio.run(main())