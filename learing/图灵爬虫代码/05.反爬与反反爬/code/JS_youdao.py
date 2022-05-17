import requests
import hashlib
import time
import random
import json

class Youdao(object):

    def __init__(self,word):
        self.url="https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
            "Cookie": "OUTFOX_SEARCH_USER_ID=-1130617441@10.110.96.158; JSESSIONID=aaaii2cv_xEdE5M57FEay; OUTFOX_SEARCH_USER_ID_NCOO=525910394.6538928; fanyi-ad-id=305426; fanyi-ad-closed=1; ___rl__test__cookies=1649779157469",
            "Host": "fanyi.youdao.com",
            "Origin": "https://fanyi.youdao.com",
            "Referer": "https://fanyi.youdao.com/"
        }
        self.formdata=None
        self.word=word

    def generate_formdata(self):
        """
        return {
            ts: r="" + (new Date).getTime()
            salt: ts + parseInt(10 * Math.random(), 10),
            sign: n.md5("fanyideskweb" + self.word + salt + "Ygy_4c=r#e#4EX^NUGUc5")
        }
        """
        ts=str(int(time.time()*1000))
        salt=ts+str(random.randint(0,10))
        tempstr="fanyideskweb" + self.word + salt + "Ygy_4c=r#e#4EX^NUGUc5"
        md5=hashlib.md5()
        md5.update(tempstr.encode())
        sign=md5.hexdigest()
        self.formdata={
    "i": self.word,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": salt,
    "sign":sign,
    "lts": ts,
    "bv": "7e897500afcde4988ba75227fa754c55",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
}

    def get_data(self):
        response=requests.post(self.url,data=self.formdata,headers=self.headers)
        return response.content

    def parse_data(self):
        _data=self.get_data()
        data=json.loads(_data)
        return data['translateResult'][0][0]['tgt']

    def run(self):
        #url
        #headers
        #formdata
        self.generate_formdata()
        #发送请求，获取响应
        data=self.get_data()
        #解析数据
        result=self.parse_data()
        # print(result)
        return result

if __name__ == '__main__':
    youdao=Youdao("大家好")
    result=youdao.run()
    print(result)