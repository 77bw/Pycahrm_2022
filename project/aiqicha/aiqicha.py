#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Organization  : CCR DataCenter
# @Time          : 2022/2/23
# @Author        : LZP
# @File          : main.py
# @Function      : 批量挖掘企业地址
import requests
import re
import json
import pymysql
import pymongo
import random
from setting import MYSQL,MONGODB
# from company_name import COMPANY
from mongo import MongoClient

class StandardV2Pipeline:
    def count(self, table,kk, param=None):
        try:
            count = self.cursor.execute(f"SELECT * FROM `{table}` WHERE `{kk}` = '{param}'")
            self.conn.commit()
            return count
        except:
            self.conn.rollback()

    def main(self,key_word):
        self.conn = pymysql.Connect(host=MYSQL['host'], port=MYSQL['port'], user=MYSQL['user'],
                                    passwd=MYSQL['passwd'], db=MYSQL['db'], charset='utf8')
        self.cursor = self.conn.cursor()

        params = {
            "q": key_word,
            "t": "",
            "p": '1',
            "s": "1",
            "o": "0",
            "f": "{}"
        }
        headers = {
            "User-Agent": "User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Referer": "https://aiqicha.baidu.com/s?q=%E6%95%B0%E6%8D%AE&t=0"  # 防盗链

        }
        cookies = {
    "_j47_ka8_": "57",
    "_y18_s21_": "9aedd6ab",
    "_s53_d91_": "39f92fe2a7f7b984758929acec0481974e60e27e4ae1d9a1a4fe6afa8fd8fe5cc9a94f5adab5a753bd083f21a56ae67bf6d65db52419a448807d074d489c4e106cb81e6c33176b1c2475d7c05176c3ef630bc3ee796076581f1229253fd5cf6bcb46e4a3f94daf32fff0d67d79e5a6c507af4295d9648b1f5465285f2e8afbde3d036aeadf1bd321d2e0bdbe0fdee7899482157fc8d6534a599103e7d107e3c94a579965018451b78f38a332bc004f5063de955a5f5c21c3f8afd6451c6e1127f8ee810ccc30fa10a4de005d290b672d",
    "BIDUPSID": "F1699AE9264DFF72712115B010275FDF",
    "PSTM": "1641377506",
    "BAIDUID": "F1699AE9264DFF723E27F5FBA667B3DA:FG=1",
    "__yjs_duid": "1_34b09f2afdd8a3fdc9139746fabfa21c1641452734070",
    "BDORZ": "B490B5EBF6F3CD402E515D22BCDA1598",
    "BAIDUID_BFESS": "2CE562358170FE5785CBBB9432CAE596:FG=1",
    "BDPPN": "a1d72c8fdb3e6903823ac8e7a7dd7f8b",
    "log_guid": "abd65e65812fb9ee64c83dcf5f004618",
    "ZX_UNIQ_UID": "a3d4a993a1c219b78586249d24433503",
    "Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf": "1649294934,1649311808",
    "ZX_HISTORY": "[{\"visittime\":\"2022-04-07+15:19:55\",\"pid\":\"xlTM-TogKuTw-uGAT4AzrdKPDJmEWE*amQmd\"},{\"visittime\":\"2022-04-07+14:10:07\",\"pid\":\"xlTM-TogKuTwecOmNqs7sTo1Swq*XY4h3wmd\"}]",
    "BDUSS": "1mYWw1UnRBY01QRzl0V2FDUHhGWlpudFB5djlhUW4xRzNwNEduMkRsU1dIM1ppSVFBQUFBJCQAAAAAAAAAAAEAAAC~qU91cG9yaXplMzU5NTM3MTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJaSTmKWkk5iNm",
    "BDUSS_BFESS": "1mYWw1UnRBY01QRzl0V2FDUHhGWlpudFB5djlhUW4xRzNwNEduMkRsU1dIM1ppSVFBQUFBJCQAAAAAAAAAAAEAAAC~qU91cG9yaXplMzU5NTM3MTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJaSTmKWkk5iNm",
    "_t4z_qc8_": "xlTM-TogKuTwOPzNsMlpKn03Vtko8fGOWwmd",
    "ab164931480": "2050adf4babbbff66043d390f66fb25b1649317036851",
    "_fb537_": "xlTM-TogKuTwWCdG57O08DICGTa5cWNe2orPZeTIXzk2md",
    "ab164931840": "2250adf4babbbff66043d390f66fb25b1649318655054",
    "Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf": "1649318655",
    "ab_sr": "1.0.1_MmQ3NDcyYjU1NzAyYzYxNWQ1Yjk0NTBlOGVlZmIyNDQ4NzY1ODg1MDMwZDZjNGIwM2JkNTMyM2ExMjUyNzZlNmEzMjAzYzczZjU1ODRhMDkwYjM0ZTU4ZDMyNjdlYmMwOGYxNTJmOGFkNWJkYzRkODg0MjA5MzJmMjljOWE5NTQ1MGQ2NGM1MDQzN2FlNDlmODQ5ZTlmYmVmMjRkNGZhZg==",
    "RT": "\"z=1&dm=baidu.com&si=gmi7n5ugut4&ss=l1opqr5h&sl=1&tt=cu&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=1tr&cl=5i1\""
}
        url = "https://aiqicha.baidu.com/s/advanceFilterAjax"
        count = self.count('company','name',param="拼多多")
        if count == 0:
            try:
                response = requests.get(url, headers=headers, cookies=cookies ,params=params)
                result=response.json()["data"]["resultList"]
                for i in len(result):
                    _pid = response.json()["data"]["resultList"][i]['pid']
                    pid = decrypt_pid(_pid)
                    _headers = {
                        "Connection": "keep-alive",
                        "sec-ch-ua": "^\\^",
                        "sec-ch-ua-mobile": "?0",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
                        "Accept": "application/json, text/plain, */*",
                        "ymg_ssr": "1646031633558_1646037792782_asoOVGiIlJJDjZ+z3RC78+ArPxITOVsXGuBM0DV3WtY+I/MOAdIS0+FfFF3qg8miR/3sbVSqcmWkwQ5wDotBNDKpzBh6nidLMEOVjyv80Qd3oIjuRt30nG+xFpjF1knHPVrQNIm+7naoSgq0ZfzBUxyV1WHTP7kSyH7pwHEmhiWjG3sWzF+mdR3L649OZaSIClh0XM2gcywRIAtDLuuVVSmaB5HhM0hRM3ZVT60qhRwm+ORkovG7HNSq3vjZHhyJ75AZ86WmRqrsoVbOwN0Tpyk76HDoIynmX3MONSVqQtHNOvY1yqVyJdHyG46dxBj0NacsWsthqDgeq9tu+66Fww==",
                        "X-Requested-With": "XMLHttpRequest",
                        "Zx-Open-Url": "https://aiqicha.baidu.com/company_detail_31263653269918",
                        "sec-ch-ua-platform": "^\\^Windows^^",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Dest": "empty",
                        "Referer": "https://aiqicha.baidu.com/company_detail_31263653269918",
                        "Accept-Language": "zh-CN,zh;q=0.9"
                    }
                    _params = {
                        "pid": pid
                    }
                    _url = "https://aiqicha.baidu.com/detail/basicAllDataAjax"
                    response = requests.get(_url, headers=_headers, cookies=cookies, params=_params)


                    try:
                        # _resultList = re.findall('window.pageData = (.*?"position":""})', response.text)[0]
                        _resultList = response.json()['data']['basicData']
                        # _resultList =  json.loads(_resultList)['result']
                        # print(_resultList['regNo'], _resultList['district'],
                        #       _resultList['prevEntName'], _resultList['entName'],
                        #       _resultList['regAddr'])
                        entname = _resultList['entName']
                        try:
                            unifiedCode = _resultList['unifiedCode']
                        except:
                            unifiedCode = None
                        openStatus = _resultList['openStatus']
                        legalPerson = _resultList['legalPerson']
                        try:
                            telephone =_resultList['telephone']
                            print(telephone)
                        except:
                            telephone = None
                        try:
                            email = _resultList['email']
                        except:
                            email = None
                        sql = f'INSERT INTO `company` (`entname`, `unifiedcode`, `openstatus`, `legalperson`, `telephone`, `email`,`name`)VALUES ("{entname}", "{unifiedCode}", "{openStatus}", "{legalPerson}", "{telephone}", "{email}", "{"拼多多"}")'
                        self.cursor.execute(sql)
                        self.conn.commit()
                        print(_resultList['entName'],_resultList['telephone'],_resultList['email'],_resultList['openStatus']
                              ,_resultList['legalPerson'],_resultList['unifiedCode'])
                    except:
                        pid = decrypt_pid_2(_pid)
                        # params_2 = {
                        #     "pid": pid
                        # }

                        url = f"https://aiqicha.baidu.com/company_detail_{pid}"
                        response = requests.get(url, headers=headers, cookies=cookies)
                        _resultList = re.findall('window.pageData = (.*?"position":""})', response.text)[0]
                        # _resultList = response.json()['data']['basicData']
                        _resultList = json.loads(_resultList)['result']
                        # print(_resultList['regNo'], _resultList['district'],
                        #       _resultList['prevEntName'], _resultList['entName'],
                        #       _resultList['regAddr'])
                        entname = _resultList['entName']
                        unifiedCode = _resultList['unifiedCode']
                        openStatus = _resultList['openStatus']
                        legalPerson = _resultList['legalPerson']
                        try:
                            telephone =_resultList['telephone']
                        except:
                            telephone = None
                        try:
                            email = _resultList['email']
                        except:
                            email = None
                        sql = f'INSERT INTO `company` (`entname`, `unifiedcode`, `openstatus`, `legalperson`, `telephone`, `email`,`name`)VALUES ("{entname}", "{unifiedCode}", "{openStatus}", "{legalPerson}", "{telephone}", "{email}", "{"拼多多"}")'
                        self.cursor.execute(sql)
                        self.conn.commit()
                        print(_resultList['entName'],_resultList['telephone'],_resultList['email'],_resultList['openStatus']
                              ,_resultList['legalPerson'],_resultList['unifiedCode'])

            except:
                pass
        else:
            print("已经存在")



        # if resultList:
        #     sql3 = f"UPDATE `spider`.`punishment` SET `admin_counter_addr` = '无' WHERE `admin_counter_name` = '{key_word[0]}'"
        #     self.cursor.execute(sql3)
        #     self.conn.commit()
            #     print(key_word[0], '无地址')
        # else:
        #     # resultList = response.json()["data"]["resultList"]
        #     if len(resultList) != 0:
        #         for item in resultList:
        #             name = item['entName'].replace('em','').replace('<','').replace('>','').replace('/','')
        #             address = item['domicile'].replace('em','').replace('<','').replace('>','').replace('/','')
        #             credit = item['regNo'].replace('em','').replace('<','').replace('>','').replace('/','')
        #             credit = decrypt_credit(credit)
        #             print(address)
        #             sql =f"UPDATE `spider`.`punishment` SET `admin_counter_addr` = '{address}' WHERE `admin_counter_name` = '{key_word[0]}'"
        #             self.cursor.execute(sql)
        #             self.conn.commit()
        #             break
        #     else:
        #         sql2 = f"UPDATE `spider`.`punishment` SET `admin_counter_addr` = '无' WHERE `admin_counter_name` = '{key_word[0]}'"
        #         self.cursor.execute(sql2)
        #         self.conn.commit()
        #         print(key_word[0],'无地址')
#
# def get_cookies():
#     mongodb = MongoClient(**MONGODB)
#     search_res = mongodb.find("aqc_cookies", {'_id': {'$exists': True}}, {'_id': 0, 'cookies': 1}).limit(1)
#     cookies = list(search_res)[0]['cookies']
#     # print(cookies)
#     del mongodb
#     return cookies

def decrypt_pid(_str):
    a = 0
    for i in _str:
        if i.isdigit():  #检测输入的字符串是否只由数字组成。
            if i == '4':
                _str = replace_char(_str, '6', a)
            elif i == '5':
                _str = replace_char(_str, '8', a)
            elif i == '6':
                _str = replace_char(_str, '9', a)
            elif i == '7':
                _str = replace_char(_str, '4', a)
            elif i == '8':
                _str = replace_char(_str, '5', a)
            elif i == '9':
                _str = replace_char(_str, '7', a)
        else:
            _i = i
            _str = replace_char(_str, str(_i), a)
        a = a + 1
    return _str

def decrypt_pid_2(_str):
    a = 0
    for i in _str:
        if i.isdigit():
            if i == '0' or i == '1' or i == '2' or i == '3':
                _str = replace_char(_str, i, a)
            elif i == '4' or i == '6' or i == '8':
                _i = int(i) + 1
                _str = replace_char(_str, str(_i), a)
            elif i == '5' or i == '7' or i == '9':
                _i = int(i) - 1
                _str = replace_char(_str, str(_i), a)
        else:
            _i = i
            _str = replace_char(_str, str(_i), a)
        a = a+1
    return _str

def replace_char(old_string, char, index):
    '''
    字符串按索引位置替换字符
    '''
    old_string = str(old_string)
    # 新的字符串 = 老字符串[:要替换的索引位置] + 替换成的目标字符 + 老字符串[要替换的索引位置+1:]
    new_string = old_string[:index] + char + old_string[index+1:]
    # print(new_string)
    return new_string
if __name__ == '__main__':
        StandardV2Pipeline().main('拼多多')

