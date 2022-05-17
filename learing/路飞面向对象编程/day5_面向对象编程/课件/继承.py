

class Animal:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


class People(Animal):

    def walk(self):
        print("People [%s] is walking..." % self.name)


class Pig(Animal):

    def eat(self):
        print("Pig [%s] is eating..." % self.name)


class Dog(Animal):

    def eat(self):
        print("Dog [%s] is eating..." % self.name)


person = People("Alex",25,"Male")
pig = Pig("Mjj",4,"公")
dog = Dog("毛毛",3,"母")

person.walk()
pig.eat()
dog.eat()