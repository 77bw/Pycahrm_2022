from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.set_default_timeout()  #设置全局的timeout，改为0，永不超时

    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input:has-text("百度一下")
    page.locator("input:has-text(\"百度一下\")").click()
    # expect(page).to_have_url("https://www.baidu.com/")

    # Click text=新闻
    with page.expect_popup() as popup_info:
        page.locator("text=新闻").click()
    page2 = popup_info.value

    # Click text=百度一下 帮助 >> input[name="word"]
    page2.locator("text=百度一下 帮助 >> input[name=\"word\"]").click()

    # Click [aria-label="标题：广州市公布新增3例本土确诊病例详情"]
    with page2.expect_popup() as popup_info:
        page2.locator("[aria-label=\"标题：广州市公布新增3例本土确诊病例详情\"]").click()
    page3 = popup_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
