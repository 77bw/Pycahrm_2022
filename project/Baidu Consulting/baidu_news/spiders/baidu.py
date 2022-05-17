import scrapy
from datetime import datetime, timedelta
from baidu_news.utils.util import time_datil,url
from baidu_news.items import BaiduNewsItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    start_urls= url

    def parse(self, response):
        print(response)
        # 时间筛选在d之前,将时间格式都转换为字符串进行比较
        d = '2022-02-11 00:00:00'
        date = (datetime.strptime(d, "%Y-%m-%d %H:%M:%S")).strftime("%Y-%m-%d %H:%M:%S")
        item = BaiduNewsItem()
        divs = response.xpath("//div[@id='content_left']/div[position()>1]")

        for div in divs:
            title = div.xpath('.//h3/a')
            title = title.xpath('string(.)').get().replace("\n","").replace(" ","")
            href = div.xpath('.//h3/a/@href').get()
            #大标题content获得内容进行分割
            summary = div.xpath('.//span[2]/text()').getall()
            summary="".join(summary)
            # sources=content[0]
            # dateTime=content[1]
            # summary=content[2]
            sources=div.xpath('.//*[@class="c-color-gray"]/text()').extract_first()
            dateTime=div.xpath('.//div/span[1]/text()').extract_first()

            dateTime = time_datil.parseTime(dateTime)

            if dateTime > date:
                item['title']=title
                item['dateTime'] = dateTime
                item['sources'] = sources
                item['href'] = href
                item["summary"] = summary

                print(title, dateTime, sources, href, summary)
                yield item
            else:
                return 0
        # 翻页操作
        url = response.xpath('//div[@id="page"]/div/a[last()]/@href').get()
        page=response.xpath('//*[@id="page"]/div/strong/span[2]/text()').get()
        next_page = "https://www.baidu.com" + url

        if next_page:
            print("正在爬取第{}页,url:".format(int(page)+1)+next_page)
            yield scrapy.Request(next_page, callback=self.parse)

if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl baidu".split()
    cmdline.execute(args)
