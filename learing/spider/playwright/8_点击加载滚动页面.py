from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.gzdaily.cn/amucsite/web/index.html#/home')

    for i in range(3):
        page.evaluate("window.scrollTo(0,document.body.scrollHeight)")# 将滚动条调整至页面底部循环三次
        page.wait_for_timeout(2000)
        page.click('//*[@class="btn ng-scope"]')
        page.wait_for_timeout(3000)

        page.wait_for_load_state('networkidle')
    html = page.content()
    print(html)
    browser.close()