#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
共通库
作用：把常用的方法写在这里库方便其他库调用
时间：2018-03-26
"""
import os
import re
import hashlib


# 全局变量定义区
# 定义获取当前路径全局变量
gCurDir = os.path.split(os.path.realpath(__file__))[0]
# 日志文件的目录
gFileName = gCurDir + '\\Log\\'
# 报告文件的目录
gReportName = gCurDir + '\\report\\'
# 生成的二维码目录
gQrDir = gCurDir+'\\QrImgs\\'


# 去空格
def delSpace(data):
    """
    利用正则去掉字符换里的空格
    参数：data为一个字符串
    如:a bc=>abc
    """
    return re.sub('[ ]', "", data)


# 去掉/r/n
def delEnter(data):
    """
    利用正则去掉字符换里的换行符
    参数：data为一个字符串
    如:a\r\nb=>ab
    """
    return re.sub('[\r\n]', "", data)


# 去掉/r/n\
def delEnterAndLine(data):
    """
    利用正则去掉字符换里的换行符和转义\\
    参数：data为一个字符串
    如:a\r\n\\b=>ab
    """
    return re.sub('[\r\n\\]', "", data)


# 去掉空格\r\n
def delSpaceEnter(data):
    """
    正则\\s:空白字符，包括（空格，\t\r\n\f\v)
    """
    return re.sub(r"\s", "", data)


# 替换~号为,
def repBLH(data):
    """
    利用正则替换~号为，号
    参数：data为一个字符串
    如：a~b=>a,b
    """
    return re.sub('~', ",", data)


# xor加密解密
def jiemi(data):
    key = 'x2L0K1j8'
    dLen = len(data)
    kLen = len(key)
    a = ""
    for i in range(dLen):
        keyIndex = i % kLen
        a += chr(ord(data[i]) ^ ord(key[keyIndex]))
    return a


# hash1加密
def hash1Encode(codeStr):
    hashobj = hashlib.sha1()
    hashobj.update(codeStr.encode('utf-8'))
    return hashobj.hexdigest()


# parameters参数化
def change_parameters(data):
    data = data.split(',')
    a = ""
    for i in range(len(data)):
        a += data[i]
        if i == len(data)-1:
            break
        a = a + '&'
    return a


# 预期返回参数data中有多层嵌套时的数据处理
def change_check_data(data):
    n = []
    for i in range(0, len(data)):
        b = data[i].split('~')
        n.append(b)
    return n
