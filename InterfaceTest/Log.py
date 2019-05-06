#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
日志库
作用：把日志的基本功能写在这里供逻辑调用
时间：2019-03-21
"""
import Common
import os
import time


# 写入日志文件
def writeLog(fName, data):
    """
    作用：每次执行时记载当前逻辑运行的日志
    参数：fName 日志文件名 data 要写入的字符串
    逻辑：对指定的日志文件按追加的方式写入，内容包括 当前时间 字符串 换行
    """
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print now_time
    fName = fName[:-5]
    with open(Common.gFileName+fName+'_log.txt', 'ab+') as f:
        # 将str转成bytes类型
        cont = now_time + ':' + data + '\r\n'
        cont = bytes(cont, encoding='utf-8')
        f.write(cont)


# 重置日志文件
def resetLogFile(fName):
    """
    作用：每次执行都会累加许多过去的日志，故在执行前清理掉过去的日志
    参数：fName 日志文件名
    逻辑：目标路径存在指定日志文件则删除掉
    """
    fName = fName[:-5]
    if os.path.exists(Common.gFileName+fName+'_log.txt'):
        os.remove(Common.gFileName+fName+'_log.txt')
