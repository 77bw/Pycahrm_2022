class A:
    __N = 0  # 类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A__N

    def __init__(self):
        self.__X = 10  # 变形为self._A__X

    def __foo(self):  # 变形为_A__foo
        print('from A')

    def bar(self):
        self.__foo()  # 只有在类内部才可以通过__foo的形式访问到.

# A._A__N是可以访问到的，即这种操作并不是严格意义上的限制外部访问，仅仅只是一种语法意义上的变形

a = A()


a._A__N = 3

print(a._A__N)
a.__Y = "test"

print(a.__Y)



class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__life_val = 100

    def got_attack(self): # 只能通过方法去修改私有变量
        self.__life_val -= 20
        print("got attack ....,life val drops 20, got %s left.." %self.__life_val)

p = Person("Jack",22)
p.got_attack()





