"""
python中sql插入数据的格式为list[tuple(),tuple(),tuple()]或者tuple(tuple(),tuple(),tuple())

"""

import pymysql
import re
import json
from pprint import pformat
import ssl
import traceback
import time
# 全局取消ssl证书验证
ssl._create_default_https_context = ssl._create_unverified_context
_regexs = {}

class MysqlClient(object):
    def __init__(self,host,user,password,db):
        """
        初始化mysql进行连接
        """
        self.conn = pymysql.connect(host=host,
                               user=user,
                               password=password,
                               db=db,
                               charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()  # 执行完毕返回的结果集默认以元组显示

    def __del__(self):
        self.cursor.close()
        self.conn.close()
    # def close_conn(self):
    #     '''结束查询和关闭连接'''
    #     self.cursor.close()
    #     self.conn.close()
    def list2str(self,datas):
        '''
        列表转字符串
        :param datas: [1, 2]
        :return: (1, 2)
        '''
        data_str = str(tuple(datas))
        data_str = re.sub(",\)$", ')', data_str)
        return data_str

    def get_jsonData(self, data):
        """单独针对于接口提取的data来获取json的数据信息"""
        keys = ['`{}`'.format(key) for key in data["result"]['items'][0].keys()]
        keys = self.list2str(keys).replace("'", '')
        values = [tuple(data["result"]['items'][i].values()) for i in range(0, len(data["result"]['items']))]
        return keys, values

    def get_info(self,html, regexs, allow_repeat=True, fetch_one=False, split=None):
        regexs = isinstance(regexs, str) and [regexs] or regexs

        infos = []
        for regex in regexs:
            if regex == '':
                continue

            if regex not in _regexs.keys():
                _regexs[regex] = re.compile(regex, re.S)

            if fetch_one:
                infos = _regexs[regex].search(html)
                if infos:
                    infos = infos.groups()
                else:
                    continue
            else:
                infos = _regexs[regex].findall(str(html))

            if len(infos) > 0:
                # print(regex)
                break

        if fetch_one:
            infos = infos if infos else ('',)
            return infos if len(infos) > 1 else infos[0]
        else:
            infos = allow_repeat and infos or sorted(set(infos), key=infos.index)
            infos = split.join(infos) if split else infos
            return infos

    def get_json(self,json_str):
        '''
        @summary: 取json对象
        ---------
        @param json_str: json格式的字符串
        ---------
        @result: 返回json对象
        '''

        try:
            return json.loads(json_str) if json_str else {}
        except Exception as e1:
            try:
                json_str = json_str.strip()
                json_str = json_str.replace("'", '"')
                keys = self.get_info(json_str, "(\w+):")
                for key in keys:
                    json_str = json_str.replace(key, '"%s"' % key)

                return json.loads(json_str) if json_str else {}

            except Exception as e2:
                print(e2)

            return {}

    def dumps_json(self,json_, indent=4):
        '''
        @summary: 格式化json 用于打印
        ---------
        @param json_: json格式的字符串或json对象
        ---------
        @result: 格式化后的字符串
        '''
        try:
            if isinstance(json_, str):
                json_ = self.get_json(json_)

            json_ = json.dumps(json_, ensure_ascii=False, indent=indent, skipkeys=True)

        except Exception as e:
            # log.error(e)
            json_ = pformat(json_)

        return json_

    def format_sql_value(self,value):
        """
        转换为json格式（字符串）
        :param value:
        :return:
        """
        if isinstance(value, str):
            #对字符串进行转义escape_string，防止插入mysql转义问题
            value = pymysql.escape_string(value)

        elif isinstance(value, list) or isinstance(value, dict):
            value = self.dumps_json(value, indent=None)

        elif isinstance(value, bool):
            value = int(value)

        return value

    def insert_many(self,table,data):
        """ 插入数据到mysql
        data:为插入的数据
        批量插入多条数据
        """

        try:
            keys,values=self.get_jsonData(data)
            result=','.join(['%s'] * len(data["result"]['items'][0]))
            sql='insert into {table}{keys} values ({result})'.format(table=table,keys=keys,result=result)
            self.cursor.executemany(sql,values)
            self.conn.commit()
            print("插入数据完毕")
        except:
            self.conn.rollback()
            traceback.print_exc()

    def insert_one(self,table,data):
        """ 插入数据到mysql
           data:为插入的数据
           批量插入多条数据
           """
        try:
            keys, values = self.get_jsonData(data)
            result = ','.join(['%s'] * len(data["result"]['items'][0]))
            sql = 'insert into {table}{keys} values ({result})'.format(table=table, keys=keys, result=result)
            for i in values:
                self.cursor.execute(sql, i)
                self.conn.commit()
            print("插入数据完毕")
        except:
            self.conn.rollback()
            traceback.print_exc()

    def find_one(self, condition):
        """
        查找单条数据
        cursor对象还提供了3种提取数据的方法：fetchone、fetchmany、fetchall.。每个方法都会导致游标动，所以必须注意游标的位置。
        cursor.fetchone():获取游标所在处的一行数据，返回元组，没有返回None
        cursor.fetchmany(size):接受size行返回结果行。如果size大于返回的结果行的数量，则会返回cursor.arraysize条数据。
        cursor. fetchall():接收全部的返回结果行。
        :param table:
        :param condition:查询的sql语句条件  sql='select * from demo where legalPersonName=\'赵坤\''
        :return :为输出每一行的记录
        """
        try:
            self.cursor.execute(condition)
            result = self.cursor.fetchone()
            while result != None:
                print(result, self.cursor.rownumber)
                result = self.cursor.fetchone()
        except:
            self.conn.rollback()
            traceback.print_exc()

        return result

    def find(self, condition):
        """
        查找全部数据
        :param condition: 查询的sql语句条件
        :return: result结果为一个列表
        """
        try:
            keys, values = self.get_jsonData(data)
            # 执行SQL语句
            self.cursor.execute(condition)
            res = self.cursor.fetchall()
            for i in res:
                print(i)
            print('共 %d条数据' % len(res))
            # 获取所有记录列表
            # print(keys)
            # result=[it for it in results]

        except:
            self.conn.rollback()
            traceback.print_exc()

    def update_one(self, condition):
        """
        更新单条数据
        :param condition:sql='update demo set regCapital="10万" where legalPersonName=\'刘计平\''
        :return:
        """
        try:
            self.cursor.execute(condition)
            print('更新成功')
            self.conn.commit()
        except:
            self.conn.rollback()
            traceback.print_exc()

    def update(self, condition, data):
        """
        :param condition: 更新的sql語句  'update demo set regCapital=%s where legalPersonName=%s'
        :param data: 你要更新進去的語句可以是列表裏面其嵌套元組，或者元組嵌套元組  [('有钱人','刘计平'),('暴富','赵坤')]
        :return:
        """
        # 更新数据
        try:
            self.cursor.executemany(condition, data)
            print('更新成功')
            self.conn.commit()
        except:
            self.conn.rollback()
            traceback.print_exc()


    def delete(self, condition, data):
        """
        :param condition: 更新的sql語句  'delete from  demo  where legalPersonName=%s'
        :param data: 你要更新進去的語句可以是列表裏面其嵌套元組，或者元組嵌套元組  [('刘计平')]
        :return:
        """
        try:
            self.cursor.executemany(condition, data)
            print('删除成功')
            self.conn.commit()
        except:
            # 发生错误时回滚
            self.conn.rollback()
            traceback.print_exc()



if __name__ == '__main__':
    data = [
        {
            "regStatus": "存续",
            "estiblishTime": 1374681600000,
            "regCapital": "0万人民币",
            "name": "北京百度网讯科技有限公司南京分公司",
            "logo": "https://img5.tianyancha.com/logo/lll/010c44218af9a39e745a400850b48af0.png@!f_200x200",
            "alias": "北京百度",
            "id": 139573097,
            "category": "724",
            "personType": 1,
            "legalPersonName": "赵坤",
            "base": "js"
        },
        {
            "regStatus": "注销",
            "estiblishTime": 1336406400000,
            "regCapital": "",
            "name": "北京百度网讯科技有限公司哈尔滨分公司",
            "logo": "https://img5.tianyancha.com/logo/lll/5ed7edde6ac52f84fed757e78a23c49f.png@!f_200x200",
            "alias": "北京百度",
            "id": 1615756664,
            "category": "642",
            "personType": 1,
            "legalPersonName": "向海龙",
            "base": "hlj"
        },
        {
            "regStatus": "注销",
            "estiblishTime": 1330617600000,
            "regCapital": "",
            "name": "北京百度网讯科技有限公司西安分公司",
            "logo": "https://img5.tianyancha.com/logo/lll/1e21bc076c4f1629d8de5be85fd0e2cb.png@!f_200x200",
            "alias": "北京百度",
            "id": 1566690935,
            "category": "659",
            "personType": 1,
            "legalPersonName": "向海龙",
            "base": "snx"
        },
        {
            "regStatus": "注销",
            "estiblishTime": 1326211200000,
            "regCapital": "",
            "name": "北京百度网讯科技有限公司重庆分公司",
            "logo": "https://img5.tianyancha.com/logo/lll/53b97676f92b3ea6b7f37babdfbea680.png@!f_200x200",
            "alias": "北京百度",
            "id": 412551136,
            "category": "653",
            "personType": 1,
            "legalPersonName": "向海龙",
            "base": "cq"
        },
        {
            "regStatus": "在业",
            "estiblishTime": 1211212800000,
            "regCapital": "",
            "name": "北京百度网讯科技有限公司广州分公司",
            "logo": "https://img5.tianyancha.com/logo/lll/e94da5a7b0bb926632ac585766028e6f.png@!f_200x200",
            "alias": "北京百度",
            "id": 139572971,
            "category": "653",
            "personType": 1,
            "legalPersonName": "沈抖",
            "base": "gd"
        },
        {
            "regStatus": "在业",
            "estiblishTime": 1210780800000,
            "regCapital": "",
            "name": "北京百度网讯科技有限公司东莞分公司",
            "logo": "https://img5.tianyancha.com/logo/lll/762a5d7bd8f3a41a6ea39bbad6d946f0.png@!f_200x200",
            "alias": "北京百度",
            "id": 139573020,
            "category": "732",
            "personType": 1,
            "legalPersonName": "沈抖",
            "base": "gd"
        },
        {
            "regStatus": "存续",
            "estiblishTime": 1209916800000,
            "regCapital": "",
            "name": "北京百度网讯科技有限公司上海分公司",
            "logo": "https://img5.tianyancha.com/logo/lll/33c94402e09f1b2d027057f1ba61957f.png@!f_200x200",
            "alias": "北京百度",
            "id": 711249800,
            "category": "751",
            "personType": 1,
            "legalPersonName": "沈抖",
            "base": "sh"
        },
        {
            "regStatus": "注销",
            "estiblishTime": 1209398400000,
            "regCapital": "",
            "name": "北京百度网讯科技有限公司佛山分公司",
            "logo": "https://img5.tianyancha.com/logo/lll/809d933b2ef0d6392274daab2fa0c24d.png@!f_200x200",
            "alias": "北京百度",
            "id": 2456357709,
            "category": "642",
            "personType": 1,
            "legalPersonName": "刘计平",
            "base": "gd"
        },
        {
            "regStatus": "存续",
            "estiblishTime": 1208448000000,
            "regCapital": "",
            "name": "北京百度网讯科技有限公司深圳分公司",
            "logo": "https://img5.tianyancha.com/logo/lll/8e1aa6e84ff617657c2eeadae5b451f0.png@!f_200x200",
            "alias": "北京百度",
            "id": 139572921,
            "category": "652",
            "personType": 1,
            "legalPersonName": "沈抖",
            "base": "gd"
        }]
    # insert_many('demo',data)
    # sql='select * from demo where legalPersonName=\'赵坤\''
    # find(sql)
    sql_conn=MysqlClient(host='localhost',
                               user='root',
                               password='123456',
                               db='test')
    # sql = 'select * from demo where legalPersonName=\'赵坤\''
    # sql = 'update demo set regCapital="10万" where legalPersonName=\'刘计平\''
    # sql='update demo set regCapital=%s where legalPersonName=%s'
    # data=[('有钱人','刘计平'),('暴富','赵坤')]
    sql_conn.insert_many('demo',data)
    # result=sql_conn.find_one(sql)
    # print(result)
    # sql_conn.find(sql)
    # sql_conn.update(sql,data)
