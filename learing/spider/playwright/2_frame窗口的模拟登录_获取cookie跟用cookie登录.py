from playwright.sync_api import Playwright, sync_playwright
import json

# def run(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://mail.qq.com/")
#     #登录
#     # page.fill('//*[@id="u"]','1329696875')
#     # page.fill('//*[@id="p"]','3214836abcdefg')
#
#     #通过选择器获得login_frame进行登录，iframe剥离，直接切换到iframe窗口就可以
#     login_frame = page.query_selector('//*[@id="login_frame"]').content_frame()
#     login_frame.fill('//*[@id="u"]', '1329696875')
#     login_frame.fill('//*[@id="p"]','3214836abcdefg')
#
#     login_frame.click('//*[@id="login_button"]')
#     #设置局部变量
#     page.wait_for_timeout(3000)  #相当于time.sleep(3)
#
#     # 获得登录后 cookie
#     storage = context.storage_state()
#     with open("state.json", "w") as f:
#         f.write(json.dumps(storage))
#
#     context.close()
#     browser.close()
#
# with sync_playwright() as playwright:
#     run(playwright)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)

    # 加载状态
    with open("state.json") as f:
        storage_state = json.loads(f.read())
    context = browser.new_context(storage_state=storage_state)

    # Open new page
    page = context.new_page()

    # Go to http://www.glidedsky.com/login
    page.goto("https://mail.qq.com/cgi-bin/frame_html?sid=GnGzdOS-XRx7OXYU&r=39db8b449c6b6b015409b8fd2d8ef5ef")

    html=page.content()
    print(html)
    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

