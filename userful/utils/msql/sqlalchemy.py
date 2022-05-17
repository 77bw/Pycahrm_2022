from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer



Base = declarative_base()
class Engine:
    def __init__(self, conn):
        self.engine = create_engine(conn, encoding='utf8')  # 这engine直到第一次被使用才真实创建

class ORM(Engine):
    """对象关系映射（Object Relational Mapping）"""
    def __init__(self, conn):
        super().__init__(conn)
        _Session = sessionmaker(bind=self.engine)  # 创建ORM基类
        self.session = _Session()  # 创建ORM对象
        self.Base = Base
        self.create_all()

    def __del__(self):
        self.session.close()

    def create_all(self):
        """创建所有表"""
        self.Base.metadata.create_all(bind=self.engine)

    def drop_all(self):
        """删除所有表"""
        self.Base.metadata.drop_all(bind=self.engine)

    def add(self, Table, dt):
        """
        :param Table: 创建表的类名
        :param dt: 插入数据为字典
        :return:
        """
        self.session.add(Table(**dt))
        self.session.commit()  # 提交

    def add_all(self,  Table, dt):
        """
         添加多个数据,插入为列表add_all
        :param items: students=[]
        :param dt: dt=[{'Sno': '10001', 'Sname': 'Frnak', 'Ssex': 'M', 'Sage': 22, 'Sdept': 'SFS'},
                    {'Sno': '10001', 'Sname': 'Frnak', 'Ssex': 'M', 'Sage': 22, 'Sdept': 'SFS'},
                    {'Sno': '10001', 'Sname': 'Frnak', 'Ssex': 'M', 'Sage': 22, 'Sdept': 'SFS'}]
        :return:
        """
        for i in dt:
            self.session.add(Table(**i))  # 添加到ORM对象
            self.session.commit()  # 提交

    def fetchall(self, data):
        """   可获取表所有的数据  查询得到的item_list是一个包含多个Student对象的列表,需要显示数据需要遍历
        获取指定字段的所有数据 一个列表里面的所有内容
        :param Table: 表名,字段名 传入的字数必须为元组
        :return:  #  数据
        for item in data:
            print(item.Sno, item.Sname, item.Ssex, item.Sage, item.Sdept)
        """
        item_list=self.session.query(*data).all()
        return item_list

    def query(self, data,condition):
        """
        :param data: 表名,字段名 传入的字数必须为元组
        :param condition:  进行判断的过滤条件必须为元组
        :return:  获取所有进行过滤条件的数据
        """
        ## student=session.query(Student.Sname).filter(Student.Ssex == 'M').all()
        item_list=self.session.query(*data).filter(*condition).all()
        return item_list

    def count(self, Table,condition):
        """
        :param Table: 传入表名
        :param condition 进行判断的过滤条件必须为元组
        :return: 获取指定数据的行数
        """
        #session.query(Student).count()
        count = self.session.query(Table).filter(*condition).count()
        return count

    def update(self, Table, condition, dt):
        """有则更新，没则插入"""
        q = self.session.query(Table).filter(*condition)
        if q.all():
            q.update(dt)  # 更新
            self.session.commit()  # 提交
        else:
            self.add(Table,dt)

    def delete(self, data,condition):
        """删除指定数据"""
        q = self.session.query(data).filter(*condition)
        #session.delete( Person(name='张三', age=18))
        if q.all():
            q.delete()
            self.session.commit()
            print("删除成功")
        else:
            print("你筛选的数据不在")

if __name__ == '__main__':
    class Student(Base):  # 必须继承declaraive_base得到的那个基类
        __tablename__ = "Students"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
        # 表的结构
        Sno = Column(String(10), primary_key=True)  # Column类创建一个字段
        Sname = Column(String(20), nullable=False, unique=True,
                       index=True)  # nullable(可为空的)就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
        Ssex = Column(String(2), nullable=False)
        Sage = Column(Integer, nullable=False)
        Sdept = Column(String(20))

    orm=ORM('mysql+pymysql://root:123456@localhost:3306/demo')

    # 增加单条数据 add
    # data={'Sno': '10001', 'Sname': 'Frnak', 'Ssex': 'M', 'Sage': 22, 'Sdept': 'SFS'}
    # orm.add(Student,data)

    #增加多条数据，插入类型为列表里面嵌套字典
    # data=[{'Sno': '10003', 'Sname': 'V', 'Ssex': 'f', 'Sage': 24, 'Sdept': 'SFS'},
    #       {'Sno': '10001', 'Sname': 'Frnak', 'Ssex': 'M', 'Sage': 22, 'Sdept': 'SFS'}]
    # orm.add_all(Student, data)

    #查询所有数据
    # data=orm.fetchall((Student,))
    # print(data)
    # for item in data:
    #     print(item.Sno, item.Sname, item.Ssex, item.Sage, item.Sdept)
    #查询指定列的所有数据
    # data=(Student.Sname,Student.Ssex)
    # a=orm.fetchall(data)
    # print(a)
    #查询判断数据
    # sql= (Student.Sage >= 10,Student.Sno == '10001')
    # data=(Student,)
    # data=orm.query(data,sql)
    # for item in data:
    #     print(item.Sno, item.Sname, item.Ssex, item.Sage, item.Sdept)
    # filter(Student.Sage.in_([16, 24])
    # data=(Student,)
    # sql=( Student.Sage.in_([12, 22]),)
    # data = orm.query(data, sql)
    # for item in data:
    #     print(item.Sno, item.Sname, item.Ssex, item.Sage, item.Sdept)

    #获取表的行
    #
    # sql= (Student.Sage == 22,)
    # count=orm.count(Student,sql)
    # print(count)

    #更新数据
    # sql=(Student.Sage >= 25,)
    # dt={'Sno': '1005', 'Sname': 'fg', 'Ssex': 'f', 'Sage': 22, 'Sdept': 'dfgdfg'}
    # orm.update(Student,sql,dt)

    #删除数据
    # sql = (Student.Sage < 22,)
    # orm.delete(Student,sql)
