from playwright.sync_api import sync_playwright
import time

#第一种写法
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     # page.goto('https://www.hizh.cn/')
#     page.goto('https://spa3.scrape.center/')
#     page.evaluate(
#         """
#         var intervalID = setInterval(function () {
#             var scrollingElement = (document.scrollingElement || document.body);
#             scrollingElement.scrollTop = scrollingElement.scrollHeight;
#         }, 200);
#
#         """
#     )
#     prev_height = None
#     while True:
#         curr_height = page.evaluate('(window.innerHeight + window.scrollY)')    #
#         if not prev_height:
#             prev_height = curr_height
#             time.sleep(1)
#         elif prev_height == curr_height:
#             page.evaluate('clearInterval(intervalID)')
#             break
#         else:
#             prev_height = curr_height
#             time.sleep(1)
#
#     page.screenshot(path='电影.png', full_page=True)
#
#     # def on_response(response):
#     #     if '/api/movie/' in response.url and response.status == 200:
#     #         print(response.json())
#     #
#     # #Page 对象提供了一个 on 方法，它可以用来监听页面中发生的各个事件，比如 close、console、load、request、response 等等。
#     # # 可以监听 response 事件，response 事件可以在每次网络请求得到响应的时候触发，我们可以设置对应的回调方法。
#     # page.on('response', on_response)
#
#     browser.close()


#第二种写法
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # page.goto('https://www.hizh.cn/')
    page.goto('https://www.jd.com/')
    page.wait_for_load_state('networkidle')

    js = "document.documentElement.scrollHeight"
    # 初始化现在滚动条所在高度为0
    height = 0
    # 当前窗口总高度
    new_height = page.evaluate(js)

    while height < new_height:
        # 将滚动条调整至页面底部
        for i in range(height, new_height, 500):
            page.evaluate('window.scrollBy(0, {})'.format(i))
            time.sleep(1)
        height = new_height
        time.sleep(0.1)
        new_height = page.evaluate(js)
        
    html = page.content()
    print(html)
    browser.close()


