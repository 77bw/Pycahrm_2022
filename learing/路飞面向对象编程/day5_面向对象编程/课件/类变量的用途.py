

class Person:
    nationality = "Chinese"

    def __init__(self,name,sex,birthday,hometown):
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.hometown = hometown


p1 = Person("Alex","Male","1995-05-32","山东德州")
p2 = Person("Mjj","Ladyboy","1992-06-16","河南信阳")

print(p1.nationality,p2.nationality)

p2.nationality = "Japan"
print(p1.nationality,p2.nationality)