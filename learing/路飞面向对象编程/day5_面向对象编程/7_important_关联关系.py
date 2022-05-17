
class RelationShip:
    """保存couple之间的对象关系"""

    def __init__(self):
        self.couple = []

    def make_couple(self,obj1,obj2):
        self.couple = [obj1,obj2] # 两个人就成了对象
        print("[%s] 和 [%s] 确定了男女关系..." % (obj1.name,obj2.name))

    def get_my_parter(self,obj): # p1 p2

        #print("找[%s]的对象" % obj.name,)
        for i in self.couple:
            if i != obj: # 代表这个是obj的对象。。。
                return i
        else:
           print("你自己心里没有点数么，你没有对象。。。")

    def break_up(self):

        print("[%s] 和 [%s] 正式分手了....江湖再见...改日再约..." % (self.couple[0].name,self.couple[1].name) )
        self.couple.clear()  # 分手


class Person:
    def __init__(self,name,age,sex,relation):
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation # 在每个人的实例存储 关系对象
        #self.parter = None # 应该是一个对象 ，代表 另一半

    def do_private_stuff(self):
        pass


relation_obj = RelationShip()
p1 = Person("Mjj",24,"M",relation_obj)
p2 = Person("Lyy",22,"F",relation_obj)

relation_obj.make_couple(p1,p2) # 让2人成为对象

print(p1.relation.couple)

print(p1.relation.get_my_parter(p1).name) # 拿到mjj的对象



p1.relation.break_up()

p2.relation.get_my_parter(p2)








# # 双向绑定,关联
# p1.parter = p2 # 这样就把Lyy当做了Mjj的另一半
# p2.parter = p1
#
# print(p1.parter.name,p2.parter.name )
#
# p2.parter = None
# #p1.parter = None
#
#
# print(p1.parter,p2.parter )