#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : simple_logging_set_level.py
# Date              : 08.11.2018
# Last Modified Date: 08.11.2018
"""
logging日志模块
默认5种WARNING级别日志,只显示WARNNING级别信息
DEBUG:详细信息，调试信息
INFO:一切正常运行
WARNING:有警告或将来问题
ERROR:严重问题
CRITICAL:严重错误

"""
import logging
import time

"""
INFO级别则所有日志信息均显示出来
filename参数将创建日志文件，若不存在则创建，存在则附加其后
logging.basicConfig(level=logging.INFO, filename="my.log")
但此方法会将日志增长很快，更好的解决方法是time.strftime方法,形成格式为my-2018-11-6.log
filemode='w'可开启此模式，但会覆盖老文件,不推荐使用
"""
#  logging.basicConfig(level=logging.INFO, filename=time.strftime("my-%Y-%m-%d.log"))
#  格式化输出日志信息,使用datefmt修改日志日期格式
#  logging.basicConfig(format='%(asctime)s %(levelname)-10s %(processName)s %(name)s %(message)s',
logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] \
                    %(levelname)-10s %(processName)s %(name)s %(message)s',
                    datefmt="%Y-%m-%d-%H-%M-%S",
                    filename=time.strftime("my-%Y-%m-%d.log"))
"""
 %(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称,级别名
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0] 目录名，完整路径
 %(filename)s: 打印当前执行程序名,文件名，不含目录
 %(funcName)s: 打印日志的当前函数,函数名
 %(lineno)d: 打印日志的当前行号,行号
 %(asctime)s: 打印日志的时间 年-月-日 时-分-秒，毫秒 2013-04-26 20:10:43,745
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID
 %(processName)d: 打印进程名
 %(message)s: 打印日志信息,消息体
 %(module)s:模块名
 %(name)s:日志模块名

logging模块提供logger,handler,filter,formatter四种:
    logger:记录器，提供日志接口，供应用代码使用.最常用的操作有2类:配置和发送日志消息.
    在使用接口debug,info,warn,error,critical之前需创建logger实例,即创建记录器
    创建方法:
        logger = logging.getLogger(logger_name)
        实例创建后以下方法进行日志级别设置，增加处理器handler
        logger.setLevel(logging.ERROR) 设置日志级别为ERROR，只有日志级别大于等于ERROR的日志才会输出
        logger.addHandler(handler_name) 为logger实例增加一个处理器
        logger.removeHandler(handler_name) 为logger实例删除一个处理器
    handler:处理器，常用有3种
        StreamHandler:
            创建方法:sh = logging.StreamHandler(stream=None)
        FileHandler:
            创建方法:fh=logging.FileHandler(filename,mode='a',encoding=None,delay=False)
        NullHandler:

    filter:过滤器
    formatter:格式化器,设置日志信息最后的规则，结构和内容，默认时间格式：%Y-%m-%d%H:%M:%S
        创建方法:formatter=logging.Formatter(fmt=None,datefmt=None)
        fmt:消息的格式化字符串，不指明将使用'%(message)s'
        datefmt:日期的字符串,不指明将ISO8601日期格式
"""


logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
