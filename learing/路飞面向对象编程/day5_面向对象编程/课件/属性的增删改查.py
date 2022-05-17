
class Person:

    nationality = "Chinese"
    addr = "北京"
    def __init__(self,name,age,sex):

        self.name = name
        self.age = age
        self.sex = sex

# 实例属性操作
p = Person("Alex",26,"Male")
p.name = "Alex Li 金角大王" # 修改属性
p.job = "CEO" # 添加实例属性
del p.sex # 删除实例属性
print(p.job)  #打印添加的实例属性

# 类属性操作
Person.nationality = "US"
Person.race = "Yellow" # 添加类属性
del Person.addr

print(p.addr) # 再调用已删除的类属性就会报错了