

# 1 整合日志
def collect_logs():
    print("log on server A ,get access.log")
    print("log on server B ,get access.log")
    print("log on server C ,get access.log")
    print("combine logs in to one file")


# 2 日志分析
def log_analyze(log_file):
    print("pv、uv分析....")
    print("用户来源分析....")
    print("访问的设备来源分析....")
    print("页面停留时间分析....")
    print("入口页面分析....")


# 3 生成报告并发送
def send_report(report_data):
    print("connect email server...")
    print("send email....")


def main():
    collect_logs()
    log_analyze('my_db')
    send_report()


if __name__ == '__main__':
    main()