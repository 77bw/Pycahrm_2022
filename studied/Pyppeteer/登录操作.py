import asyncio

from faker import Faker
from pyppeteer import launch

fake = Faker()
URL = 'https://www.zhihu.com/'


async def main():
    browser = await launch({'headless': False,
                            'args': ['--disable-infobars'],
                            'userDataDir': './userdata'    #保存cookies等文件在这个下面，下次不用登录直接进入
                            })
    page = await browser.newPage()

    await page.setViewport({'width': 1530, 'height': 800})
    await page.setUserAgent(fake.user_agent())
    #Pyppeteer 的 Page 对象有一个 evaluateOnNewDocument 方法，可以在每次加载网页的时候执行某个语句，此处执行将 WebDriver 隐藏的命令
    await page.evaluateOnNewDocument('function(){Object.defineProperty(navigator, "webdriver", {get: () => undefined})}')
    await page.goto(URL)

    await asyncio.sleep(412)
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
