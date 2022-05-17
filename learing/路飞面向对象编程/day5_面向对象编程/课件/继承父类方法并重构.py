

class Animal:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("[%s] is eating..."%self.name)


class People(Animal):

    def __init__(self,name,age,sex,race):
        #Animal.__init__(self,name,age,sex) # 先执行父类方法
        super(People,self).__init__(name,age,sex)
        #super().__init__(name,age,sex)  # 跟上面这行super语法的效果一样
        self.race = race  # 再加上子类的属性
        print("初始化了一个人....")

    def walk(self):
        print("People [%s] is walking..." % self.name)


class Pig(Animal):

    def eat(self): # 对父类的方法进行了重构
        print("Pig [%s] is eating..." % self.name)


class Dog(Animal):

    def eat(self):
        print("Dog [%s] is eating..." % self.name)


person = People("Alex",25,"Male","Yellow")
pig = Pig("Mjj",4,"公")
dog = Dog("毛毛",3,"母")

person.walk()
person.eat()
pig.eat()
dog.eat()