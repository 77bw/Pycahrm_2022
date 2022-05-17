from playwright.sync_api import Playwright, sync_playwright
def run(playwright: Playwright) -> None:
    # 首先实例化一个浏览器对象
    browser = playwright.chromium.launch(headless=False)
    # 打开一个浏览器会话
    context = browser.new_context()
    # 打开一个新页面
    page = context.new_page()
    # Go to https://www.google.com.hk/?gws_rd=ssl
    page.goto("https://www.google.com.hk/?gws_rd=ssl")
    # Click [aria-label="搜索"]
    page.click("[aria-label=\"搜索\"]")
    # Fill [aria-label="搜索"]
    page.fill("[aria-label=\"搜索\"]", "playwright")
    # Press Enter
    # 这里是一个页面导航功能
    # 点击元素可以出发导航，要求使用 page.expect_navigation(**kwargs)
    # 这里点击了搜索按钮，这样页面信息可以获取浏览器新的内容
    with page.expect_navigation():
        page.press("[aria-label=\"搜索\"]", "Enter")
    # 这里由于打开了新的页面，所以需要使用page.expect_popup()来获取新的页面，并且用as来操作新的页面
    with page.expect_popup() as popup_info:
        page.click("text=Playwright: Fast and reliable end-to-end testing for modern ...")
    # 这里将新页面命名为page1，并将新的页面信息传给page1
    page1 = popup_info.value
    # 关闭浏览器会话，和浏览器
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)