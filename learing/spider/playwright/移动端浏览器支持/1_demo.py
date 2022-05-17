from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone_12_pro_max = p.devices['iPhone 12 Pro Max']  #devices 属性指定了一台移动设备，这里传入的是手机的型号
    browser = p.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_12_pro_max,
        locale='zh-CN',
        geolocation={'longitude': 116.39014, 'latitude': 39.913904},
        permissions=['geolocation']
    )    #模拟移动端浏览器，初始化一些移动设备信息、语言、权限、位置等信息，这里我们就用它来创建了一个移动端 BrowserContext 对象，
    # 通过 geolocation 参数传入了经纬度信息，通过 permissions 参数传入了赋予的权限信息，最后将得到的 BrowserContext 对象赋值为 context 变量
    page = context.new_page()
    page.goto('https://amap.com')
    page.wait_for_load_state(state='networkidle')
    page.screenshot(path='location-iphone.png')
    browser.close()