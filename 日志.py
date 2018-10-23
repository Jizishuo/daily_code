import os
import logging

BASE_DIR = BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True  # 标记是否在开发环境


# 给过滤器使用的判断
class RequireDebugTrue(logging.Filter):
    # 实现filter方法
    def filter(self, record):
        return DEBUG


LOGGING = {
    # 基本设置
    'version': 1,  # 日志级别
    'disable_existing_loggers': False,  # 是否禁用现有的记录器

    # 日志格式集合
    'formatters': {
        # 标准输出格式
        'standard': {
            # [具体时间][线程名:线程ID][日志名字:日志级别名称(日志级别ID)] [输出的模块:输出的函数]:日志内容
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][%(name)s:%(levelname)s(%(lineno)d)]\n[%(module)s:%(funcName)s]:%(message)s'
        }
    },

    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': RequireDebugTrue,
        }
    },

    # 处理器集合
    'handlers': {
        # 输出到控制台
        'console': {
            'level': 'DEBUG',  # 输出信息的最低级别
            'class': 'logging.StreamHandler',
            'formatter': 'standard',  # 使用standard格式
            'filters': ['require_debug_true', ],  # 仅当 DEBUG = True 该处理器才生效
        },
        # 输出到文件
        'log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(BASE_DIR, 'debug.log'),  # 输出位置
            'maxBytes': 1024 * 1024 * 5,  # 文件大小 5M
            'backupCount': 5,  # 备份份数
            'encoding': 'utf8',  # 文件编码
        },
    },

    # 日志管理器集合
    'loggers': {
        # 管理器
        'default': {
            'handlers': ['console', 'log'],
            'level': 'DEBUG',
            'propagate': True,  # 是否传递给父记录器
        },
    }
}
'''
-----------------日志管理器集合--------------------------------
其中键名是管理器的名称，键值是管理器的配置。
管理器需要配置3个内容：
1）handlers：必填，处理器列表，处理传递进来的日志消息用哪些处理器。
2）level：必填，日志消息处理的最低级别，处理该哪些日志消息。
3）propagate：选填，是否传递给父记录器(这个一般写True即可)。

handlers同样在日志配置里面配置，稍后详细讲解。
level是针对日志消息。日志消息存在级别，共6个。

级别由大到小分别是 CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
若设置DEBUG级别，比DEBUG高的日志消息同样会使用处理器列表中的处理器处理。
当然，网上还有些人写的配置没有写这个处理器集合内，直接将处理器写在配置字典内。
这种做法不建议，不方便维护。


------------处理器集合------------------------------
日志处理器是设置日志消息用何种方式处理，以及使用该方式所需的相关配置信息。
最常见的有3种处理方式：
1）将日志信息输出到控制台
2）将日志信息输出到文件
3）将日志信息发送邮件到指定邮箱

其中键名是处理器的名称，键值是处理器的配置。

处理器配置的内容包含4个基本设置：
1）level：该级别和日志管理器的级别一样，该配置有些重复
2）class：用何种方式处理，该类是继承了logging.handle类
3）formatter：日志内容的格式，该内容稍后讲解。
4）filter：选填，过滤器，该内容稍后讲解。
其他参数是class类初始化所需的参数。

该处理器配置内容比较清晰，我已经在上面写的标准配置写了注释，参考即可。
其中输出到文件中用到os模块和一个BASE_DIR变量，该变量是获取当前文件所在的位置。
若你先自定义自己的class处理类，继承logging.Handler类，实现emit方法即可。

-------------日志格式集合------------------------------
日志格式只需要设置format格式化文本即可。格式化文本如下：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s 用户输出的消息
'''

import logging


class TestHandler(logging.Handler):
    def __init__(self, text):
        self.text = text

    def emit(self, record):
        print("test handler %s" % self.text)  # 输出初始化传递的变量
        print(record.getMessage())  # 输出日志消息

#---------日志配置文件-------------------
import logging
import logging.config

# 加载前面的标准配置
logging.config.dictConfig(LOGGING)

# 获取loggers其中的一个日志管理器
logger = logging.getLogger("default")

# 尝试写入不同消息级别的日志信息
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")


#在合适的地方写入日志
#错误日志 try方法,  运行日志-装饰器
'''
import logging
import logging.config

# 加载前面的标准配置
logging.config.dictConfig(LOGGING)

# 获取loggers其中的一个日志管理器
logger = logging.getLogger("default")

def test():
    try:
        a = 1 / 0
    except Exception as e:
        logger.error(e.message)  # 写入错误日志

        # 其他错误处理代码
        pass

'''
import logging
import logging.config

# 加载前面的标准配置
logging.config.dictConfig(LOGGING)


# 日志记录装饰器
def recode_log(func):
    # 获取loggers其中的一个日志管理器
    logger = logging.getLogger("default")

    def warpper(*args, **kw):
        # 记录开始运行时间
        logger.debug("start %s" % func.func_name)

        # 运行方法
        func()

        # 记录结束运行时间
        logger.debug("end %s"% func.func_name)
        return warpper

    # 测试方法
    @recode_log
    def test():
        print("run test")

    if __name__ == "__main__":
        test()