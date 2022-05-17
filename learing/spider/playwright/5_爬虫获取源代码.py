from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cnblogs.com/")

    page.wait_for_load_state('networkidle')
    html = page.content()

    # 选择提取标签,获取所有的标签
    elements = page.query_selector_all('//*[@class="post-item-title"]')  #使用xpath
    for element in elements:
        print(element)
        print(element.text_content())  #.text_content()获取文本
        print(element.get_attribute('href')) #提取标签中的href属性

    #query_selector，如匹配到多个，则取第一个
    comment=page.query_selector('//*[@id="post_list"]/article[2]/section/div/a').text_content()
    print(comment)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)