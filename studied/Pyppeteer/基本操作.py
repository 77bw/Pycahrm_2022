import asyncio
from lxml import etree
#Faker可以为你伪造数据，生成随机的数据
from faker import Faker
from pyppeteer import launch

#初始化faker数据
fake = Faker()
URL = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'


async def main():
    #使用launch方法创建一个Browser对象，相当于启动浏览器  没有设置默认为无头，设置为有头，跟去掉Chrome 正受到自动测试软件的控制”，可以使用 args 参数来关闭：
    browser = await launch({'headless': False,
                            'args':['--disable-infobars']
                            })
    #调用newPage()方法新建了一个page对象，相对于浏览器新建一个选项卡
    page = await browser.newPage()

    #调用setUserAgent 设置请求头
    await page.setUserAgent(fake.user_agent())

    # Page 对象调用了 goto 方法访问目标页面，相当于在浏览器中输入目标 URL，浏览器跳转到了对应页面进行加载；
    await page.goto(URL)

    doc = etree.HTML((await page.content()))
    titles_xpath = "//div[@class='list']/a[@class='item']/div/img/@alt"
    titles = doc.xpath(titles_xpath)
    print(titles)

    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
