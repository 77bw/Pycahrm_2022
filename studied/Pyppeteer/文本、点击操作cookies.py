import asyncio

from faker import Faker
from pyppeteer import launch


async def main():
        browser = await launch(headless=False)

        page = await browser.newPage()
        await page.setViewport({'width': 1530, 'height': 800})
        await page.goto('https://www.baidu.com/')

        #输入文本使用page对象的type方法，一个参数为选择器，第二个参数为所输入的内容
        await page.type('#kw', 'Python')  # 输入文本

        #也可以用xpath来实现这个功能
        # button = await page.xpath("//*[@id=\"su\"]")
        # await button[0].click()

        #点击操作，一个参数为选择器，后面的参数button：left、middle、right；clickCount：点击次数；delay：延迟点击（ms）。
        await page.click('#su', options={
            'button': 'left',
            'clickCount': 1,
            'delay': 3000,  # 延迟点击(ms)
        })
        #page对象获取源代码使用 content 方法，获取 Cookies 使用 cookies 方法
        print(await page.content())
        print(await page.cookies())

        await asyncio.sleep(412)
        await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
