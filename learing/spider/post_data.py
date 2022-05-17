import requests
import json

url='https://api.landchina.com/tGdxm/result/list'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'Origin': 'https://www.landchina.com',
    'Referer': 'https://www.landchina.com/',
}
"""
请求首部字段 Origin 指示了请求来自于哪个站点。
Referer 首部包含了当前请求页面的来源页面的地址，即表示当前页面是通过此来源页面里的链接进入的
"""
data = {
    'endDate': "",
    'pageNum': 1,
    'pageSize': 10,
    'startDate': "",
}

response = requests.post(url, headers=headers, json=data)
print(response.text)


#第二种headers携带Content-Type，使用dumps转换成json格式并使用data=data

data=json.dumps(data)
headers={
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}
response=requests.post(url,data=data,headers=headers)
print(response.json())
