import asyncio
from pyppeteer import launch
from faker import Faker

fake=Faker()

async def main():
    browser=await launch(headless=False,args=['--disable-infobars'])#设置有头，隐藏该浏览器正在进行自动化检测
    page=await browser.newPage()#新增一个选项卡,进入百度
    await page.goto('https://www.baidu.com')
    await asyncio.sleep(3)
    page=await browser.newPage()  #在新增一个选项卡，进入b站后在进入谷歌翻译

    await page.setUserAgent(fake.user_agent())#使用fake设置伪装请求头
    await page.setExtraHTTPHeaders(headers={}) #使用setExtraHTTPHeaders加代理防止页面打不开
    #evaluateOnNewDocumentv隐藏webdriver,防止404
    await page.evaluateOnNewDocument('function(){Object.defineProperty(navigator,"webdriver",{get:() => undefined})}')
    await page.goto('https://www.bilibili.com/')
    await asyncio.sleep(3)
    await page.goto("https://translate.google.cn/?sl=en&tl=zh-CN&op=translate")

    await page.goBack() #向后
    await asyncio.sleep(2)
    await page.goForward() #向前
    await asyncio.sleep(3)
    await page.reload() #刷新
    await asyncio.sleep(5)
    await page.screenshot(path="google翻译.png")  #截屏

    pages=await browser.pages() #获取所有页面
    page1=pages[1]  #第一个选项卡0，第二个1
    await asyncio.sleep(2)
    await page1.bringToFront() #调用bringToFront切换到第一个选项卡上去
    await asyncio.sleep(3)

    await page1.close() #关闭第一页的选项卡
    await browser.close() #关闭浏览器


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
