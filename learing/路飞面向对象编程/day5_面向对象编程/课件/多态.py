# class Dog(object):
#     def sound(self):
#         print("汪汪汪.....")
#
# class Cat(object):
#     def sound(self):
#         print("喵喵喵.....")
#
#
# def make_sound(animal_type):
#     """统一调用接口"""
#     animal_type.sound() # 不管你传进来是什么动物，我都调用sound()方法
#
#
# dogObj = Dog()
# catObj = Cat()
#
# make_sound(dogObj)
# make_sound(catObj)

# class Document:
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
#
# class Pdf(Document):
#     def show(self):
#
#         return 'Show pdf contents!'
#
#
# class Word(Document):
#     def show(self):
#
#         return 'Show word contents!'
#
#
# documents = [Pdf('Document1'),
#              Pdf('Document2'),
#              Word('Document3')]
#
# for document in documents:
#     print(document.name + ': ' + document.show())


class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")


class SportsCar(Car):
    def drive(self):

        return 'Sportscar driving!'


    def stop(self):
        return 'Sportscar braking!'


class Truck(Car):
    def drive(self):

        return 'Truck driving slowly because heavily loaded.'

    def stop(self):
        return 'Truck braking!'


cars = [Truck('东风重卡'),
        Truck('三一重工'),
        SportsCar('Tesla Roadster')]

for car in cars:
    print(car.name + ': ' + car.drive())
