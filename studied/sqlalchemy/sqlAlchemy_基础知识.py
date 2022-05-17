from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine,inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#初始化数据库链接 ‘数据库类型+数据库驱动名称://用户名:密码@IP地址:端口号/数据库名’
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/demo1')
#创建对象的基类
Base = declarative_base()

class Student(Base):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "Students"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    # 表的结构
    Sno = Column(String(10), primary_key=True)  # Column类创建一个字段
    Sname = Column(String(20), nullable=False, unique=True,
                   index=True)  # nullable(可为空的)就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    Ssex = Column(String(2), nullable=False)
    Sage = Column(Integer, nullable=False)
    Sdept = Column(String(20))

    def __repr__(self):
        return "<Student>{}:{}".format(self.Sname, self.Sno)
#调用Base类的metadata方法建立所有数据库表。其中，那个repr函数是方便测试用的，可加可不加。
Base.metadata.create_all(engine)  # 这就是为什么表类一定要继承Base，因为Base会通过一些方法来通过引擎初始化数据库结构。不继承Base自然就没有办法和数据库发生联系了。
# 创建DBSession类型:
Session = sessionmaker(bind=engine)
session = Session()  # 实例化了一个会话（或叫事务），之后的所有操作都是基于这个对象的
# print(session)

#增加单条数据 add
# student = Student(Sno='10001', Sname='Frnak', Ssex='M', Sage=22, Sdept='SFS')
# session.add(student)
#添加多个数据,插入为列表add_all
# students=[
#         Student(Sno='10002', Sname='b', Ssex='d', Sage=2, Sdept='SFS'),
#         Student(Sno='10003', Sname='V', Ssex='f', Sage=24, Sdept='SFS'),
#         Student(Sno='10004', Sname='Frfbhdwk', Ssex='df', Sage=29, Sdept='SFS')
#           ]
# session.add_all(students)

# 获取表的字段名
# print(inspect(Student).c.keys())  #['Sno', 'Sname', 'Ssex', 'Sage', 'Sdept']

# 方式1: 根据id查询  返回模型对象/None
# session.query.get(4)

#查询数据
#获取所有数据
# item_list=session.query(Student).all()
# print(item_list) #查询得到的item_list是一个包含多个Student对象的列表
# for item in item_list:
#     print(item.Sno, item.Sname, item.Ssex, item.Sage, item.Sdept)


# 指定查询列  [('b',), ('Frfbhdwk',), ('Frnak',), ('V',)]
# item_list = session.query(Student.Sname).all()
# print(item_list)

# item_list = session.query(Student.Sno,Student.Sname).all()
# print(item_list)

#返回数据的第一行
# item=session.query(Student.Sno,Student.Sname).first()
# print(item)

#filter_by() 和 filter() 的最主要的区别：查询的方式不同，建议用filter这种方法使用 使用filter()方法进行筛选过滤
# student=session.query(Student.Sname).filter(Student.Ssex == 'd').all()
# print(student)
#使用order_by()进行排序
# item_list = session.query(Student.Sname, Student.Sage).order_by(Student.Sage).all() # desc()表示倒序,asc升序，如果不写默认升序
# print(item_list)
#多个查询条件（and和or）
# 默认为and, 在filter()中用,分隔多个条件表示and
# item_list = session.query(Student.Sname, Student.Sage, Student.Sno).filter(
#     Student.Sage >= 10, Student.Sno == '10001'
# ).all()
# print(item_list)  # [('Frnak', 22, '10001')]
# from sqlalchemy import or_
# # 使用or_连接多个条件
# item_list = session.query(Student.Sname, Student.Sage, Student.Sno).filter(
#     or_(Student.Sage >= 10, Student.Ssex == 'F')
# ).all()
# print(item_list)  # [('Jane', 16, 'female'), ('Ben', 20, 'male')]
#equal/like/in
# 等于
# item_list = session.query(Student.Sname, Student.Sage, Student.Ssex).filter(
#     Student.Sage == 24
# ).all()
# print(item_list)  # [('Tony', 18, 'male')]
# # 不等于
# item_list = session.query(Student.Sname, Student.Sage, Student.Ssex).filter(
#     Student.Sage != 24
# ).all()
# print(item_list)  # [('Jane', 16, 'female'), ('Ben', 20, 'male')]
# # like
# item_list = session.query(Student.Sname, Student.Sage, Student.Ssex).filter(
#     Student.Sname.like('%V%')
# ).all()
# print(item_list)  # [('Tony', 18, 'male')]
# # in
# item_list = session.query(Student.Sname, Student.Sage, Student.Ssex).filter(
#     Student.Sage.in_([16, 24])
# ).all()
# print(item_list) # [('Jane', 16, 'female'), ('Ben', 20, 'male')]

#count计算个数
# count=session.query(Student).count()
# print(count)
# count=session.query(Student).filter(Student.Ssex=="M").count()
# print(count)

#切片
# item_list=session.query(Student.Sname).all()[:2]
# print(item_list) #[('b',), ('Frfbhadwk',)]

#修改数据
# session.query(Student).filter(Student.Sno=="10001").update({'Sage':18})

#删除数据  删除数据使用delete()方法，同样也需要执行session.commit()提交事务
session.query(Student).filter(Student.Sname=="V").delete()

session.commit()  # 不要忘了commit
session.close()
