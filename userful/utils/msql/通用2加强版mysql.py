#coding:utf-8
import pymysql
class MysqlClient(object):
    def __init__(self,host,port,user,password,db):
        """
        初始化mysql进行连接
        """
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                   user=user,
                                   password=password,
                                   db=db,
                                   charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()  # 执行完毕返回的结果集默认以元组显示

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def count(self, sql, param=None):
        """SELECT COUNT(id=1) FROM demo 查询表demo的总行数  SELECT COUNT(1) FROM demo  或者 SELECT COUNT(*) FROM demo  三种写法相同
            SELECT COUNT(1) FROM demo WHERE id=139573097   查询id为139573097出现的次数
        """
        try:
            self.cursor.execute(sql, param)
            (number_of_rows,) = self.cursor.fetchone()
            return number_of_rows
        except:
            self.conn.rollback()

    def query(self, sql, param=None):
        """
        执行查询，并取出所有结果集

        :param sql:查询SQL，如果有查询条件，请指定条件列表，并将条件值使用参数[param]传递进来,
                例如: select name from user where id=%s, %s就是可变参数，需要在param中传递值
        :param param: 可选参数，tuple, list or dict
                如果param是list或者tuple, 用%s作为参数占位符.
                如果param是dict, 用%(name)s作为参数占位符。
        :param: result tuple 查询到的结果集
        """
        self.cursor.execute(sql, param)
        return self.cursor.fetchall()

    def update(self, sql, param=None):
        """
        更新记录

        :param sql: 更新SQL，如果有查询条件，请指定条件列表，并将条件值使用参数[param]传递进来,
                例如: update user set name=%s where id=%s, %s就是可变参数，需要在param中传递值
        :param param: 可选参数，tuple, list or dict
                如果param是list或者tuple, 用%s作为参数占位符.
                如果param是dict, 用%(name)s作为参数占位符。
        :param: 受影响行数
        """
        try:
            count = self.cursor.execute(sql, param)
            self.conn.commit()
            return count
        except Exception as ex:

            self.conn.rollback()
    def delete(self, sql, param=None):
        """
        删除记录,支持删除多条

        :param sql: 删除SQL，如果有查询条件，请指定条件列表，并将条件值使用参数[param]传递进来,
                例如: delete from user where id=%s, %s就是可变参数，需要在param中传递值,删除单条param=[1], 删除多条param=[1,2,3]
        :param param: 可选参数，tuple or list
                如果param是list或者tuple, 用%s作为参数占位符.
        :param: 受影响行数
        """
        try:
            count = self.cursor.executemany(sql, param)
            self.conn.commit()
            return count
        except Exception as ex:
            self.conn.rollback()
        pass
    def insert(self, sql, param=None):
        """
        插入记录

        :param sql: 更新SQL，如果有查询条件，请指定条件列表，并将条件值使用参数[param]传递进来,
                例如: insert into user(id,name,gender,age) values(%s,%s,%s,%s), %s就是可变参数，需要在param中传递值
        :param param: 可选参数，tuple or list
                如果param是list或者tuple, 用%s作为参数占位符.
        :param: 受影响行数
        """
        try:
            count = self.cursor.executemany(sql, param)
            self.conn.commit()
            return count
        except Exception as ex:
            self.conn.rollback()
        pass

    def insert_one(self,table,data):
        #这里你知道table和data，其中data是一个字典，写插入数据库的代码
        # 获取到一个以键且为逗号分隔的字符串，返回一个字符串
        try:
            if type(data) == dict:
                keys = ','.join(data.keys())
                values = ','.join(['%s'] *len(data))
                sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
                # 这里的第二个参数传入的要是一个元组
                self.cursor.execute(sql, tuple(data.values()))
                self.conn.commit()
                print(f'插入{table}成功')
            elif type(data) == list:
                keys = ','.join(data[0].keys())
                values = ','.join(['%s'] * len(data[0]))
                sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
                # 这里的第二个参数传入的要是一个元组
                for i in data:
                    self.cursor.execute(sql, tuple(i.values()))
                    self.conn.commit()
                print(f'插入{table}成功')
        except:
            self.conn.rollback()

    def insert_many(self,table, data):
        try:
            cols = ", ".join('`{}`'.format(k) for k in data[0].keys())
            # print(cols)  # '`name`, `age`'

            val_cols = ', '.join('%({})s'.format(k) for k in data[0].keys())
            # print(val_cols)

            sql = f"insert into {table}(%s) values(%s)"
            res_sql = sql % (cols, val_cols)
            self.cursor.executemany(res_sql, data)
            self.conn.commit()
            print("插入成功")
        except:
            self.conn.rollback()

if __name__ == '__main__':
    '''
    https://blog.csdn.net/tzyyy1/article/details/93510663
    '''
    data =  {
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
        }
    dic  = {
        'positionName': 'Java开发工程师 (MJ000426)',
        'salary': '10k-18k',
        'city': '深圳',
        'workYear': '1-3年',
        'education': '本科及以上',
        'jobNature': '全职',
        'positionLables': '科技金融',
        'positionAdvantage': '五险一金,带薪年假,节日福利',
        'positionDetail': '岗位职责：>1.参与嘉联支付系统研发（交易、风控、清算、创新产品），共同打造云原生支付系统解决方案。>2.对需求具有一定的分析和设计能力。>3.开发文档文档的撰写、维护。>4.根据技术接口文档编写良好的Java代码，设计并执行单元测试。>5.配合集成测试，日常生产问题定位及解决。>任职资格：>1.本科及以上学历，计算机、软件、数学等相关专业；>2.精通JAVA，扎实的Java编程基础，熟悉常用设计模式、多线程、JVM，包括内存模型、类加载机制以及性能优化，具有一定的系统设计、分析能力。>3.熟悉高性能、高并发、高可用性分布式系统设计，熟悉RPC、缓存、消息队列、负载均衡、分布式事务等，并能进行系统的调优和优化。>4.熟练掌握SpringBoot框架，一年以上SpringCloud微服务框架开发经验，深刻理解微服务原理及运行机制。>5.熟悉SqlServer、Mysql、Oracle等数据库，有数据库调优经验，熟悉主流多种NoSQL数据库。>6.有K8s，Istio经验优先考虑。>能力素养：>1.自信，自律。>2.良好的沟通能力。>3.良好的团队合作能力。',
        'address': '深圳南山区深圳湾科技生态园10栋B座22楼'
    }

    sql_conn=MysqlClient(host='localhost',
                                port = 3306,
                               user='root',
                               password='123456',
                               db='test')

    # sql_conn.insert_one('demo',data)
    # sql_conn.insert_many('job', data)

    # params = [
    #     (5, '摩根.弗里曼', '男', 60),
    #     (6, 'Iron Man', '男', 35)
    # ]
    # print(sql_conn.insert('insert into user(id, name, gender, age) values(%s,%s,%s,%s)', params))

    # print(sql_conn.count('SELECT COUNT(id=%s) FROM job', param=[1]))
    count=sql_conn.count('SELECT COUNT(%s) FROM demo', param=[1])
    print(count)
    # print(sql_conn.query('select city from job where id=%s', param=[1]))
    # print(sql_conn.count('SELECT COUNT(id=%s) FROM job', param=[1]))
    # print(sql_conn.update('update job set id=%s where id=%s', ['0', '1']))
    # print(sql_conn.delete('delete from job where id=%s', (1, 2)))