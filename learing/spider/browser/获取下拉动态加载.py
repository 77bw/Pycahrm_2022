from playwright.sync_api import sync_playwright
from lxml import etree

def main():
    url = "https://world.huanqiu.com/article"       #环球网文章url
    save_path = "./news.txt"                        #疫情文章和链接保存路径
    get_data(url)                                   #获取网页数据
    # parse_data(url)                                 #解析提取所需数据
    # save_data(save_path,url)                        #保存数据


def get_data(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        for i in range(3):
            page.evaluate("window.scrollTo(0,document.documentElement.scrollHeight)")  #document.documentElement.scrollHeight为浏览器所有内容高度
            page.wait_for_timeout(3000)  #相当于time.sleep(2)
        page.wait_for_load_state('networkidle')
        html = page.content()
        return html


def parse_data(url):
    titles = []                                     #爬取到的标题列表
    hrefs = []                                      #爬取到的标题链接列表
    soup = get_data(url)#获取网页源代码
    html = etree.HTML(soup)
    big_list = html.xpath("//*[contains(@class,'list-item')]")
    for list in big_list:
        titles.append(list.xpath(".//h4/text()")[0])
        hrefs.append('https://world.huanqiu.com/' + list.xpath("./a/@href")[0])
    return titles,hrefs


def save_data(save_path,url):
    titles,hrefs = parse_data(url)
    with open(save_path, 'a', encoding="utf-8") as fp:
        for i in list(range(len(titles))):
            fp.write(titles[i])
            fp.write("\n")
            fp.write(hrefs[i])

    #     f.write(titles[i])                                                           #写入疫情新闻标题列表
    #     f.write("\n")                                                                       #换行
    #     f.write(hrefs[i])                                                            #写入疫情新闻标题链接列表
    #     f.write("\n\n")
    # f.close()                                                                               #关闭

if __name__ == "__main__":
    main()
