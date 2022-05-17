import logging

#编程的方式来写一下高级的写法

# #记录器
logger = logging.getLogger('applog')
logger.setLevel(logging.DEBUG)   #要设置控制台跟文件不同的输出级别，其默认的logger必须设置为DEBUG级别，好让下级继承
# print(logger)
# print(type(logger))

#处理器handler,控制台输出
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
# print(consoleHandler)
# print(type(consoleHandler))

#文件输出，输出的路径是绝对路径  没有给handler指定日志级别，将使用logger的级别
fileHandler = logging.FileHandler(filename=' addDemo.log ',mode="w")
fileHandler.setLevel(logging.INFO)
# print(fileHandler)
# print(type(fileHandler))

# formatter格式       %(levelname)8s  8位

formatter = logging.Formatter("%(asctime)s|%(levelname)-8s|%(filename)s:%(lineno)s|%(message)s")
formatter1 = logging.Formatter("%(asctime)s|%(levelname)-8s|%(filename)s:%(lineno)s|%(name)s|%(message)s")
# print(formatter)
# print(type(formatter))

#给处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter1)
#为记录器添加处理器进行关联
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

#设置过滤器     a.bbb 其中的.是层级关系
flt=logging.Filter("a.bbb")

#过滤器关联对象
# logger.addFilter(flt)
fileHandler.addFilter(flt)

#打印日志代码
logger.debug("this is debug log")
logger.info("this is info log")
logger.warning("this is warning log")
logger.error("this is error log")
logger.critical("this is critical log")
