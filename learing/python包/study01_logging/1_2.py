import logging
#向日志输出变量
logging.basicConfig(level=logging. DEBUG)
name ="张三"
age = 18
#日志字符串格式化独有，其他三种python也有
logging.debug("姓名%s，年龄%d",name,age)

logging.debug("姓名%s，年龄%d"%(name,age))
logging.debug("姓名{}，年龄{}".format(name,age))
logging.debug(f"姓名 {name}，年龄{age}")