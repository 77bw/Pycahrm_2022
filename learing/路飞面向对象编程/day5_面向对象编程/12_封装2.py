class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def _getname(self):
        print('返回名字')
        return self.name
    def __getage(self):
        return 'Student:{}'.format(self.age)

    def message(self):
        print('In Student')
        return self.__getage()

    def __str__(self):
        return '{}:{}'.format(self.name, self.age)
        """返回一个对象的描述信息"""

class UnderStudent(Student):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.__university = university
    def __getage(self):
        return 'UnderStudent:'.format(self.age)

    def __str__(self):
        return '{}:{}:{}'.format(self.name, self.age, self.__university)

if __name__ == '__main__':
    s = Student('张三', 20)
    print(dir(s))
    print(s)
    print(s._getname())
    print(s.message())


    print('------------------------------------')
    us = UnderStudent('李四',22,'哈工大')
    print(dir(us))
    # print(us.__university)  #报错，外部不能直接调用私有属性
    print(us._UnderStudent__university)    #外部想强制调用私有属性，应实例名._类名+属性名
    us.__university ="ggs"  # 实例生成后，再创建的私用属性，并不具有私有性，是可以直接访问 的。
    print(us.__university)
    print(us)
    print(us._getname())
    print(us.message())
