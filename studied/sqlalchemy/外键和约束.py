"""
在从表中增加一个字段，指定这个字段外键的是哪个表的哪个字段就可以了。从表中外键的字段，必须和父表的主键字段类型保持一致。
外键约束，写在Colum中的关键字参数ondelete中，有以下几项：
RESTRICT ：默认约束类型，主表数据被删除会报错，阻止其删除
NO ACTION ：同RESTRICT一样
CASCADE ：级联删除，主表数据删除，从表相对应的数据随之被删除
SET NULL ：主表数据被删除，从表与之对应的数据变为NULL

注意：这里设定的约束，仅对于从sql删除有效，若从ORM层面来删除数据，将会无视外键约束，全部视为set null
注意：ForeignKey里的字符串格式不是类名.属性名，而是表名.字段名
"""

from sqlalchemy import create_engine, Column, Integer, String, func, ForeignKey,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

engine=create_engine("mysql+pymysql://root:123456@localhost:3306/test")
Base=declarative_base()
Session=sessionmaker(bind=engine)

class Grade(Base): #班级表
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True)
    gradename = Column(String(50), nullable=False)

class Person(Base):# 学生表
    __tablename__ = 'stundents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    #没有设置时默认外键为SET NULL
    # grade_id = Column(Integer, ForeignKey('grade.id'))  #注意：ForeignKey里的字符串格式不是类名.属性名，而是表名.字段名
    uid = Column(Integer,ForeignKey("grade.id",ondelete='CASCADE'))
Base.metadata.create_all(engine) #映射，要设置个engine

