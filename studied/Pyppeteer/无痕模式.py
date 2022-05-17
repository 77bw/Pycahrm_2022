"""
Browser
launch 方法返回的是 Browser 对象（浏览器对象），即 Browser 类的一个实例，其拥有许多用于操作浏览器的方法。

无痕模式
无痕模式的好处就是环境干净，不与其他的浏览器示例共享 Cache、Cookies 等内容，其开启方式可以通过 createIncognitoBrowserContext 方法，其返回一个 context 对象，用其创建新选项卡：
"""
import asyncio

from faker import Faker
from pyppeteer import launch

fake = Faker()
URL = 'https://gz.meituan.com/meishi/'


async def main():
    browser = await launch({'headless': False,
                            'args': ['--disable-infobars'],
                            'userDataDir': './userdata'
                            })
    context = await browser.createIncognitoBrowserContext()  #设置无痕模式
    page = await context.newPage()

    await page.setViewport({'width': 1530, 'height': 800})
    await page.setUserAgent(fake.user_agent())
    await page.evaluateOnNewDocument('function(){Object.defineProperty(navigator, "webdriver", {get: () => undefined})}')
    await page.goto(URL)

    await asyncio.sleep(412)
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
