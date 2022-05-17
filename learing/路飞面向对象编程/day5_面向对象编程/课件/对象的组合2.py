class BirthDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period


class Teacher:
    def __init__(self, name, gender, birth, course):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.course = course

    def teaching(self):
        print('teaching.....',self.course.name)


p1 = Teacher('Alex', 'Male',
             BirthDate('1995', '1', '27'),
             Course('Python', '28000', '5 months')
             )

print(p1.birth.year, p1.birth.month, p1.birth.day)

print(p1.course.name, p1.course.price, p1.course.period)
