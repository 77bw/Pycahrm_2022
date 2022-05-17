import datetime

class School(object):
    """总部，学校类"""

    def __init__(self,name,addr,website):
        self.name = name
        self.addr = addr
        self.website = website
        self.balance = 0
        self.branches = [] # 存所有的分校对象
        self.class_list = []  # 存班级列表
        self.staff_list = []  # 存员工列表
        print("创建了校区[%s], 地址:[%s]" %(name,addr))

    def count_stu_num(self):
        pass

    def count_staff_num(self):
        pass

    def staff_enrollment(self,staff_obj):
        self.staff_list.append(staff_obj)
        print("[%s]入职新员工[%s],职位[%s],部门[%s]" %(self.name,staff_obj.name,staff_obj.position,staff_obj.dept))

    def count_total_revenue(self):
        print("-----校区总收入----")
        total_rev = self.balance
        print(self.name,self.balance)
        for b in self.branches:
            print(b.name,b.balance)
            total_rev += b.balance
        print("各校区总收入:%s"%total_rev)

    def count_class_list(self):
        print("-----各校区班级----")
        print(self.name,self.class_list)
        for i in self.branches:
            print(i.name,i.class_list)

    def pay_salary(self):
        print("开始发6月工资啦....")
        for i in self.staff_list:
            i.balance += i.salary # 发工资
            self.balance -= i.salary # 总部相应账户扣钱
            print("给%s 发了 %s, 他的余额：%s" %(i.name,i.salary,i.balance))

        print("公司余额：",self.balance)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class BranchSchool(School):
    """分校"""
    def __init__(self,name,addr,website,headquarter_obj):
        super().__init__(name,addr,website)
        self.headquarter = headquarter_obj # 总部的对象
        self.headquarter.branches.append(self) # 把自己加入到总校的校区列表里，建立总部-》分校的反向关联



class Course(object):
    """课程类"""
    def __init__(self,name,price,outline):
        self.name = name
        self.price = price
        self.outline = outline
        print("创建了课程[%s],学费[%s]" %(name,price))


class Class(object):
    """班级"""
    def __init__(self,course_obj,semester,school_obj):
        self.course_obj = course_obj
        self.semester = semester
        self.school_obj = school_obj
        self.stu_list = [] # 存放学员列表

        school_obj.class_list.append(self) # 把自己加到校区的班级列表
        print("校区[%s]创建了班级[%s][%s]学期" %(school_obj.name,course_obj.name,semester))

    def stu_transfer(self,stu_obj,new_class_obj):
        """
        学员转校
        :param stu_obj: 学员对象
        :param new_class_obj: 转到的新班级的对象
        :return:

        """

    def __str__(self):
        return "%s-%s-%s学期" %(self.school_obj.name,self.course_obj.name,self.semester)
    def __repr__(self):
        return "%s-%s-%s学期" %(self.school_obj.name,self.course_obj.name,self.semester)


class Staff(object):
    """员工"""
    def __init__(self,name,age,balance,salary,position,dept,school_obj):
        self.name = name
        self.age= age
        self.balance = balance
        self.salary = salary
        self.position = position
        self.dept = dept
        self.school_obj = school_obj
        school_obj.staff_enrollment(self) # 办入职

    def punch_card(self):
        pass


class Teacher(Staff):

    def __init__(self,name,age,balance,salary,position,dept,school_obj,course_obj):
        super().__init__(name,age,balance,salary,position,dept,school_obj)
        self.course_obj = course_obj # 老师可以讲的课

    def teach_class(self,class_obj,day):
        print("老师[%s]正在班级[%s]上第[%s]天课ing..."%(self.name,class_obj,day))


class Student(object):
    """学员"""
    def __init__(self,name,age,balance,class_obj):
        self.name = name
        self.age = age
        self.balance = balance
        self.class_obj = class_obj

        # 加入班级
        class_obj.stu_list.append(self)
        # 交学费
        class_obj.school_obj.balance += class_obj.course_obj.price
        self.balance -= class_obj.course_obj.price

        print("班级[%s]加入了新学员[%s], 交了学费[%s]" %(class_obj,name,class_obj.course_obj.price))

    def punch_card(self):
        print("%s:学员在班级[%s]上课了...." %( datetime.datetime.now(), self.class_obj))



# 创建校区
headquarter = School("老男孩IT教育集团","北京昌平沙河","oldboyedu.com")
sh1_school = BranchSchool("张江校区","上海张江","oldboyedu.com",headquarter)
sh2_school = BranchSchool("虹桥校区","上海虹桥火车站","oldboyedu.com",headquarter)
sz1 = BranchSchool("骑士计划","深圳大学城","oldboyedu.com",headquarter)
luffy = BranchSchool("路飞学城","北京长安街","luffycity.com",headquarter)


# 创建课程
py_course = Course("Python",21800,None)
linux_course = Course("Linux",19800,None)
test_course = Course("Testing",19800,None)
go_course = Course("GO",22800,None)
# 创建 班级

py_24 = Class(py_course,24,headquarter)
go_5 = Class(go_course,5,headquarter)
py_12 = Class(py_course,12,sh1_school)
linux_63 = Class(linux_course,63,sz1)

# 创建员工、老师、学员
s1 = Staff("Alex",26,0,4000,"CEO","总经办",luffy)
s2 = Staff("Todd",45,0,60000,"CEO","总经办",headquarter)
s3 = Staff("明月",24,0,7000,"HR","HR",headquarter)

t1 = Teacher("日天",28,0,30000,"讲师","教学部",sz1,py_course)
t2 = Teacher("Egon",28,0,30000,"讲师","教学部",sh1_school,go_course)
t3 = Teacher("佩奇",29,0,40000,"学科带头人","教学部",headquarter,linux_course)


stu1 = Student("春生",22,50000,py_24)
stu2 = Student("black girl",22,30000,go_5)
stu3 = Student("小强",22,35000,go_5)
stu4 = Student("小虎",28,38000,linux_63)
stu5 = Student("小虎2",28,38000,py_12)
stu6 = Student("小虎3",28,38000,linux_63)

print(headquarter.balance)
print(sz1.balance)

print(headquarter.branches)
# 统计 总收入，学员人数
headquarter.count_total_revenue()
headquarter.count_class_list()

headquarter.pay_salary()