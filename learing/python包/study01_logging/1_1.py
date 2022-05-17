import logging


#默认日志的输出的级别为warning
#使用baseConfig()来指定日志输出的方式
#logging是为多线程的，跟print输出互抢资源，但是logging输出的顺序是有序的

print("this is print log")
#指定日志的输出的级别
# logging.basicConfig(level=logging.DEBUG)

#日志输为文件。默认是追加加入，w为重新写入
logging.basicConfig(filename="demo.log",filemode="w",level=logging.DEBUG)

logging.debug("this is debug log")
#DEBUG:root:this is debug log
# DEBUG:为日志级别  root：为记录器的名字
logging.info("this is info log")
logging.warning("this is warning log")
logging.error("this is error log")
logging.critical("this is critical log")