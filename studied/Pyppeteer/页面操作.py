"""Page
Page 对象即一个选项卡，对应一个页面。

提取网页资源
成功访问网页后，可以通过 Page 对象的 xpath 方法提取资源，并使用 getProperty 方法和 .jsonValue() 获取资源：
"""
import asyncio
from faker import Faker
from pyppeteer import launch

fake = Faker()
URL = 'https://www.zhihu.com/'


async def main():
    browser = await launch({'headless': False,
                            'args': ['--disable-infobars'],
                            'userDataDir': './userdata'
                            })
    page = await browser.newPage()

    await page.setViewport({'width': 1530, 'height': 800})
    await page.setUserAgent(fake.user_agent())
    await page.evaluateOnNewDocument('function(){Object.defineProperty(navigator, "webdriver", {get: () => undefined})}')
    await page.goto(URL)

    title_elements = await page.xpath("//div[contains(@class,\"Card\")]//a[@target=\"_blank\"]")
    for element in title_elements:
        title = await (await element.getProperty('textContent')).jsonValue()
        url = await (await element.getProperty('href')).jsonValue()
        print(title)
        print(url)

    await asyncio.sleep(433)
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
