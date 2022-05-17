import logging
#输出格式和添加一些公共信息
#format是logging自带的格式，其key也是自带的
#datefmt是其自己进行修改的
logging.basicConfig(format="%(asctime)s /%(levelname)s/%(filename)s : %(lineno)s|%(message)s" ,
                    datefmt="%Y-%m-%d %H:%M :%S",level=logging. DEBUG)
# 2022-04-14 14:33 :06 /DEBUG/1_3.py : 11|姓名张三，年龄18
#  时间                 日志等级  文件名  调式行数  调式信息
name ="张三"
age = 18
logging.debug("姓名%s，年龄%d ", name,age)
logging.warning("姓名%s，年龄%d ", name,age)