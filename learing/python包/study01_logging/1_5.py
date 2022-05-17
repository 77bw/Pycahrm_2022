import logging
import logging.config
#编程的方式来写一下高级的写法

# #记录器

def getLogging(confName = "applog"):
    logging.config.fileConfig("logging.conf")
    return logging.getLogger(confName)