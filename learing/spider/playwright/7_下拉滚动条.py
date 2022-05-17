from playwright.sync_api import sync_playwright
import time

#第一种写法

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://www.hizh.cn/')
#     for i in range(3):
#         page.evaluate("window.scrollTo(0,document.body.scrollHeight)")  # 将滚动条调整至页面底部循环三次
#         time.sleep(2)
#
#     page.wait_for_load_state('networkidle')
#     html = page.content()
#     print(html)
#     browser.close()

#第二种写法
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.hizh.cn/')
    # locator = page.locator("div.news-item")
    # count = locator.count()
    page.wait_for_selector("div.news-item")
    page.evaluate("window.scrollBy(0, document.body.scrollHeight)")  # 将滚动条调整至页面底部循环三次
    # page.wait_for_selector("div.news-item:nth-child({})".format(int(count+1)))
    page.wait_for_selector("div.news-item:nth-child({})".format(page.evaluate('document.getElementsByClassName(\'news-item clink\').length') + 1))
    page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
    page.wait_for_timeout(3000)
    page.screenshot(path='hizhu.png', full_page=True)


    page.wait_for_load_state('networkidle')
    html = page.content()
    print(html)
    browser.close()