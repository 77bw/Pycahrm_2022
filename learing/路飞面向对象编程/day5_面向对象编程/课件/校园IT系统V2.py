

import datetime


class School(object):
    """学校类"""
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.staff_list = [] # 存储员工对象
        self.class_list = [] # 班级列表
        self.branches = [] # 分校列表

        print("创建了学校:%s ,地址:%s"% (name,addr))



    def pay_salary(self):
        """发工资"""
        pass

    def count_staff_num(self):
        """统计员工人数"""
        pass

    def count_stu_num(self):
        """统计学员人数"""
        pass

    def new_staff_enrollment(self,staff_obj):
        """新员工入职"""
        self.staff_list.append(staff_obj)
        print("%s 入职新员工: %s , 职位:%s, 部门:%s " %(self.name,staff_obj.name,staff_obj.position,staff_obj.dept))


class BranchSchool(School):
    """分校"""
    def __init__(self,name,addr,headquarter):
        super().__init__(name,addr)
        self.headquarter = headquarter # obj
        headquarter.branches.append(self) # 把自己加到总校


class Course(object):
    """课程"""

    def __init__(self,name,price):
        self.name = name
        self.price = price
        #self.outline =
        print("创建了一个课程:%s, 学费:%s" %(self.name,self.price))


class Class(object):
    """班级"""
    def __init__(self,semester,course_obj,school_obj):
        self.semester = semester
        self.course_obj = course_obj
        self.school_obj = school_obj
        self.school_obj.class_list.append(self ) # 添加校区
        print("在[%s]校区，开设了[%s][%s]期" %(self.school_obj.name, course_obj.name,semester))

        self.stu_list = []

    def create_teaching_record(self):
        pass

    def __str__(self):
        return "%s-%s-%s" %( self.school_obj.name,self.course_obj.name,self.semester)


class Staff(object):
    def __init__(self,name,age,position,salary,dept,school_obj):
        self.name= name
        self.age = age
        self.position = position
        self.salary = salary
        self.dept = dept
        self.school_obj = school_obj
        self.school_obj.new_staff_enrollment(self)

    def punch_card(self):
        print("%s: 员工[%s]在[%s]上班打卡" %( datetime.datetime.now(), self.name,self.school_obj.name))


class Teacher(Staff):

    def teaching(self,class_obj):
        pass


class Student(object):

    def __init__(self,name,age,balance):
        self.name = name
        self.age = age
        self.balance = balance

    def enroll_class(self,class_obj):
        class_obj.stu_list.append(self)
        self.balance -= class_obj.course_obj.price # 扣学费
        print("学员%s加入了班级%s,交学费%s" % ( self.name, class_obj,class_obj.course_obj.price))


# 开学校

headquarter = School("老男孩总部","北京昌平沙河")
luffy_branch = BranchSchool("路飞学城","北京长安街",headquarter)
sh_branch = BranchSchool("上海分校1","张江",headquarter)
sh2_branch = BranchSchool("上海分校2","虹桥",headquarter)
sz_branch = BranchSchool("深圳分校","大学城",headquarter)

# 生成课程

py_course = Course("Py开发脱产",22800)
linux_course = Course("Linux脱产",19800)
go_course = Course("GO周未",5980)


# 生成班级

py24 = Class("24",py_course,sh_branch)
linux62 = Class("62",linux_course,sz_branch)


# 生成员工、老师、学员
s = Staff("日天",26,"HR",8000,"HR Dept",headquarter)
t1 = Teacher("egon",25,"Teacher",8000,"教学 Dept",sh2_branch)

stu1 = Student("春生",24,50000)
stu1.enroll_class(py24)


stu2 = Student("春生2",24,50000)
stu2.enroll_class(linux62)

stu3 = Student("春生3",24,50000)
stu3.enroll_class(py24)


# 统计总班级数

for i in headquarter.branches:
    print("-----校区:%s-----"%i.name)
    for c in i.class_list:
        print(c)
