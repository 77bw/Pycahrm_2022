"""
mysql级别的外键，还不够ORM，必须拿到一个表的外键，然后通过这个外键再去另外一张表中查找，这样太麻烦了。
SQLAlchemy提供了一个relationship，这个类可以定义属性，以后在访问相关联的表的时候就直接可以通过属性访问的方式就可以访问得到了。
因为外键(ForeignKey)始终定义在多的一方.如果relationship定义在多的一方,那就是多对一,一对多与多对一的区别在于其关联(relationship)的属性在多的一方还是一的一方，
如果relationship定义在一的一方那就是一对多.
"""
from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
import random

engine=create_engine("mysql+pymysql://root:123456@localhost:3306/demo")
Base=declarative_base()
Session=sessionmaker(bind=engine)
class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
	# 关联，默认为一对多，有外键的是多，被引的是一，这个地方写的是类名 可以通过backref来指定反向访问的属性名称
    #relationship写在哪一方都可以 对于Book，每个对象都关联一个Author对象，所以其关联类型就是其Author
    # 而对于Author，因为其关联了多个对象，所以关联类型是列表
    # 注意：relationship的第一个参数写的不是表名，而是关联的ORM类名
    books = relationship('Book', backref='author')

    def __repr__(self):
        return '<Author:(id={}, name={})>'.format(self.id, self.name)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    # 外键，表名.字段名
    author_id = Column(Integer, ForeignKey('author.id'))
    # 关联，默认为一对多，有外键的是多，被引的是一，这个地方写的是类名
    # author = relationship("Author", backref="books")

    def __repr__(self):
        return '<Book:(id={}, name={}, author_id={})>'.format(self.id, self.name, self.author_id)
session=Session()
# 插入数据
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
# author1 = Author(name='张三')
# author2 = Author(name='李四')
# book1 = Book(name='python从入门到入坟', author_id=1)
# book2 = Book(name='如何让富婆喜欢你', author_id=1)
# session.add_all([author1, author2, book1, book2])
# session.commit()
# session.close()

# 查找
# book = session.query(Book).get(1)  #get() ， 根据主键ID获取对象，若对象不存在会返回空
# print(book.author)
# author = session.query(Author).get(1)
# print(author.books)

# # 关联插入
# 因为我们ORM处理的都是类和对象，所以对于有外键的类，我们都不喜欢直接给外键赋值，而希望可以用对象关联来自动给外键赋值，sqlalchemy确实有实现这样的功能，
# 向数据库增加一条数据后，其关联属性的对象也会跟着加入，例如
# 插入数据
author1 = Author(name='张三')
author2 = Author(name='李四')
book1 = Book(name='python从入门到入坟')
book2 = Book(name='如何让富婆喜欢你')
book3 = Book(name='朝花夕拾')
# # 关联插入
# author1.books.append(book1)#列表添加
# author1.books.append(book2)
book3.author = author2#直接赋值
#
# session.add(author1)
# session.add(book3)
# session.commit()
#
# 查找
book = session.query(Book).get(3)
print(book.author)
author = session.query(Author).get(3)
print(author.books)
