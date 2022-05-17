from playwright.sync_api import sync_playwright
import re

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(headless=False)

    #ancel_request 方法可以接收两个参数，一个是 route，代表一个 CallableRoute 对象，另外一个是 request，代表 Request 对象。
    # 这里我们直接调用了 route 的 abort 方法，取消了这次请求，所以最终导致的结果就是图片的加载全部取消了
    # 不加载图片
    def cancel_request(route):
        route.abort()

    #调用了 route 方法，第一个参数通过正则表达式传入了匹配的 URL 路径，这里代表的是任何包含 .png 或 .jpg  的链接，遇到这样的请求，会回调 cancel_request 方法处理
    page.route(re.compile(r"(\.png)|(\.jpg)"), cancel_request)

    page.goto("https://spa6.scrape.center/")
    page.wait_for_load_state('networkidle')
    #截屏
    page.screenshot(path='no_picture.png')
    browser.close()