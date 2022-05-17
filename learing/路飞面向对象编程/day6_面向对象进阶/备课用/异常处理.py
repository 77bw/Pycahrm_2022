

try:
    """your code"""
except Exception:
    """上面的程序执行出错后就指行这里的代码"""

# while True:
#     num1 = input('num1:')
#     num2 = input('num2:')
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         result = num1 + num2
#     except Exception as e:
#         print('出现异常，信息如下：')
#         print(e)


# dic = ["wupeiqi", 'alex']
# try:
#     dic[10]
# except IndexError as e:
#     print(e)
#

# info = {"name":"小猿圈","website":"http://apeland.cn"}
#
# try:
#     info["addr"]
# except KeyError as e :
#     print(e)


# 未捕获到异常，程序直接报错

# s1 = 'hello'
# try:
#     #int(s1)
#     print(d)
#     pass
# except IndexError as e:
#     print(e)
#
# except KeyError as e:
#     print(e)
#
# except ValueError as e:
#     print(e)
#
# except Exception as e:
#     print("最后的万能异常",e)
#
# else:
#     print("没发生异常")
#
# finally:
#     print("无论是否有错误 ，都执行")


class MyException(BaseException):
    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise MyException("我的错误")

except MyException as e:
    print(e)


# assert  type(1) is int
# assert  1+1 == 2
# assert  1+1 == 3 #


def my_interface(name,age,score):
    assert type(name) is str
    assert type(age) is int
    assert type(score) is float

my_interface("alex",22,89.2)
