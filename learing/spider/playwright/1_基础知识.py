from playwright.sync_api import Playwright, sync_playwright
#sync_playwright 同步方式
def run(playwright: Playwright) -> None:
    # 首先实例化一个浏览器对象，headless是否显示浏览器，默认是TRUE不显示
    browser = playwright.chromium.launch(headless=False)
    # 打开一个浏览器会话
    context = browser.new_context()
    #timeout为ms，等待3s
    # context.set_default_timeout(3000)  #设置全局的timeout，改为0，永不超时
    # 打开一个新页面
    page = context.new_page()
    page.goto("https://www.baidu.com/")

    # 通过xpath定位在搜索框中输入"广州疫情", locator定位页面元素，返回的是locator对象
    page.fill("//*[@name=\"wd\"]","广州疫情")
    # page.click('//*[@id="su"]')
    page.wait_for_timeout(3000)  #相当于time.sleep(3)

    page.click('//*[@id="su"]')
    print(page.title())
    # # 这里由于打开了新的页面，所以需要使用page.expect_popup()来获取新的页面，并且用as来操作新的页面
    # with page.expect_popup() as popup_info:
    #     page.click('//*[@id="su"]')
    # # 这里将新页面命名为page1，并将新的页面信息传给page1
    # page1 = popup_info.value
    # print(page1.title())


    #选择框的选择
    # page.select_option('//*[@id="province"] ','25579')
    # page.select_option('//*[@id="city"] ', '25580')

    # 关闭浏览器会话，和浏览器
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


# page.fill("input[name=\"wd\"]", "nba")