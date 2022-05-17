"""
relationship写在一方就行了，不用写两边，容易出现同名错误
一对一的关系：
在sqlalchemy中，如果想要将两个模型映射成一对一的关系，那么应该在父模型中，指定引用的时候，要传递一个uselist=False这个参数进去。
就是告诉父模型，以后引用这个从模型的时候，不再是一个列表了，而是一个对象了。示例代码如下：
"""
from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

engine=create_engine("mysql+pymysql://root:123456@localhost:3306/demo")
Base=declarative_base()
Session=sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)
    extend = relationship("UserExtend",backref="user",uselist=False)   # # 一对一的情况，这里要设置下,uselist设置成false,关闭列表让一对多，变成一对一的关系
    def __repr__(self):
        return "<User(username:%s)>" % self.username

class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(Integer,ForeignKey("user.id"))

session=Session()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

#关联插入
user = User(username='xiaowu')
extend_user = UserExtend(school='大渡口中学')
user.extend=extend_user   #两边的关联属性都直接赋值即可
session.add(user)


session.commit()
session.close()