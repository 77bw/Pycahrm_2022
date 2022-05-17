"""
多对多的关系：
根据数据库的指示，多对多的关系，应该采用加入一张中间表的方式来解决，中间表使用Table类来创建
多对多的关系需要通过一张中间表来绑定他们之间的关系。

先把两个需要做多对多的模型定义出来
使用Table定义一个中间表，中间表一般就是包含两个模型的外键字段就可以了，并且让他们两个来作为一个“复合主键”。
在两个需要做多对多的模型中随便选择一个模型，定义一个relationship属性，来绑定三者之间的关系，在使用relationship的时候，需要传入一个secondary=中间表。

"""
from sqlalchemy import create_engine,Column,String,Integer,ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

engine=create_engine("mysql+pymysql://root:123456@localhost:3306/demo")
Base=declarative_base()
Session=sessionmaker(bind=engine)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    # 外键，表名.字段名
    author_id = Column(Integer, ForeignKey('tag.id'))
    # 关联，默认为一对多，有外键的是多，被引的是一，这个地方写的是类名
    # author = relationship("Author", backref="books")
    # 多对多关联，secondary指定中间表，这样的话，book中有tags，tag中有books，其关联信息的外键将放到book_tag中
    tags = relationship('Tag', backref='books', secondary='book_tag')

    def __repr__(self):
        return '<Book:(id={}, name={}, author_id={})>'.format(self.id, self.name, self.author_id)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
# 多对多中间表，第一个参数是表名，第二个参数传Base.metadata
book_tag = Table(
    'book_tag',
    Base.metadata,
    # 组合成复合主键
    Column('book_id', Integer, ForeignKey('book.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
)

session=Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

book1 = Book(name='python从入门到入坟')
book2 = Book(name='如何让富婆喜欢你')
tag1 = Tag(name='推理')
tag2 = Tag(name='言情')
book1.tags.append(tag1)
book1.tags.append(tag2)
book2.tags.append(tag1)
book2.tags.append(tag2)
session.add_all([book1, book2])
session.commit()
