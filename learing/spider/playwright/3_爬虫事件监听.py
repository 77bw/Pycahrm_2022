

from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # def on_response(response):
    #     if '/api/movie/' in response.url and response.status == 200:
    #         print(response.json())
    #
    # #Page 对象提供了一个 on 方法，它可以用来监听页面中发生的各个事件，比如 close、console、load、request、response 等等。
    # # 可以监听 response 事件，response 事件可以在每次网络请求得到响应的时候触发，我们可以设置对应的回调方法。
    # page.on('response', on_response)
    page.goto('https://spa6.scrape.center/')

    #Playwright提供了 page.wait_for_load_state() 方法，支持3种参数 load domcontentloaded 和 networkidle ，可以等待页面加载至预期状态。
    page.goto('https://spa6.scrape.center/')
    #获取网页源代码 这里获取的网页源代码，不管网页是 ajax 加载的，都是获取最终的 html。得到的是查看网页源代码，不是检查元素里面的
    #凡是需要对 html 中的元素进行操作的 page.wait_for_load_state('networkidle') 必写，用于等待 html 加载。
    page.wait_for_load_state('networkidle')
    html = page.content()
    print(html)
    browser.close()