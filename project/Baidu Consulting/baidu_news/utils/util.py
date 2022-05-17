from datetime import datetime, timedelta

# 搜索关键词
# "开门红", "开端", "奥运"
words = ["广东大学"]
url = []
for keyword in words:
    urls = "https://www.baidu.com/s?" + 'ie=utf-8&medium=0&word={}&rtt=4&bsst=1&rsv_dl=news_t_sk&cl=2&tn=news&rsv_bp=1&oq=&rsv_btype=t&f=8'.format(keyword)
    url.append(urls)


class time_datil:
#时间判断方法
    def parseTime(unformatedTime):
        if unformatedTime is None:
           unformatedTime = "今天"
        else:
            unformatedTime = unformatedTime
        if "分钟" in unformatedTime:
           minute = unformatedTime[:unformatedTime.find('分钟')]
           minute = timedelta(minutes=int(minute))
           return (datetime.now() -
                   minute).strftime("%Y-%m-%d %H:%M:%S")

        elif "今天" in unformatedTime:
           time = datetime.now()
           return time.strftime("%Y-%m-%d %H:%M:%S")

        elif "小时" in unformatedTime:
           hour = unformatedTime[:unformatedTime.find('小时')]  # 4小时前
           hour = timedelta(hours=int(hour))
           return (datetime.now() -
                   hour).strftime("%Y-%m-%d %H:%M:%S")

        elif '昨天' in unformatedTime:
           time = unformatedTime[2:]  # 昨天20:04
           hours = time.split(':')[0]
           minuters = time.split(':')[-1]
           yesterday = ((datetime.now().date()) - (timedelta(days=1))).strftime("%Y-%m-%d")
           if (len(minuters) and len(hours)) == 0:
              return yesterday
           else:
              time = str(timedelta(hours=int(hours), minutes=int(minuters)))
              return (yesterday + " " + time)
        elif '前天' in unformatedTime:
           time = unformatedTime[2:]  # 昨天20:04
           hours = time.split(':')[0]
           minuters = time.split(':')[-1]
           yesterday = ((datetime.now().date()) - (timedelta(days=2))).strftime("%Y-%m-%d")
           if (len(minuters) and len(hours)) == 0:
              return yesterday
           else:
              time = str(timedelta(hours=int(hours), minutes=int(minuters)))
              return (yesterday + " " + time)

        elif '天前' in unformatedTime:
           day = unformatedTime[:unformatedTime.find('天')]  # 6天前
           day = timedelta(days=int(day))
           return (datetime.now() -
                   day).strftime("%Y-%m-%d %H:%M:%S")
        elif '年' in unformatedTime:
            unformatedTime=unformatedTime.replace("年","-").replace("月","-").replace("日","-")
            return unformatedTime
        else:
           return "0"



