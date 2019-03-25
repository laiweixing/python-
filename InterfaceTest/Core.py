#!/usr/bin/python
# -*- coding: utf-8 -*-

# Todo：接口自动化测试
# Author：Bryce

"""
核心模块
主逻辑：获取测试用例数据、发送接口请求、比对返回数据、分析测试结果
时间：2019-3-21

"""
# 引入第三方库

import os
import re
import sys
import xlrd
import hashlib
import requests
from enum import Enum
from urllib.parse import quote

# 引入封装模块

import Common
import reportHtml
import Log as log
from ExcelHelper import modifyExcel

# 定义全局变量

#枚举服务器类型
class serverType(Enum):
    test = 1    #测试服 
    formal = 2  #正式服

# 项目地址
# ipPort = "https://thirty-eight.e-stronger.com"  #38所共享单车
ipPort = "https://bed-api.e-stronger.com/index.php?"  #广正陪护床

# 获取测试数据并执行用例
def runTest(testCaseFile):
    testCaseFile = os.path.join(Common.gCurDir + '\\TestCase',testCaseFile)    #获取用例文件路径
    if not os.path.exists(testCaseFile):
        log.error('测试用例文件不存在！！！')
        sys.exit()
    fileName = testCaseFile     #获取日志文件名
    log.resetLogFile(fileName)      #重置日志文件内容
    log.writeLog(fileName,'---------------------------------------------')
    log.writeLog(fileName,'准备执行测试用例')
    testCase = xlrd.open_workbook(testCaseFile)
    table = testCase.sheet_by_index(0)
    log.writeLog(fileName,'准备加载excel用例数据')
    for i in range(1,table.nrows):
        if table.cell(i, 8).value == 'Yes' or table.cell(i, 8).value == 'yes':
            print('第'+str(i)+'行开始执行了')
        else:
            continue    #如果第八行的数据不等于Yes或yes就跳过执行下一个用例
    
        num = int(table.cell(i, 0).value)      #获取用例编号
        api_title = Common.delEnter(table.cell(i, 1).value)     #获取测试目的
        api_host = Common.delEnter(table.cell(i, 2).value)       #获取接口地址路径    
        url = Common.delEnter(table.cell(i,3).value)         #获取服务器ip
        method = Common.delEnter(table.cell(i, 4).value)     #获取请求类型
        parameters = Common.delEnter(table.cell(i, 5).value)        #获取传入参数及值
        encryption = Common.delEnter(table.cell(i, 6).value)        #获取加密方式
        returnVal = Common.delEnter(table.cell(i, 7).value)         #判断是否有返回值
        data_type = Common.delEnter(table.cell(i, 8).value)        #获取预期返回的数据类型
        data = Common.delEnter(table.cell(i, 9).value)          #获取预期返回的数据
        activity = Common.delEnter(table.cell(i, 10).value)          #判断是否执行此条用例

        log.writeLog(fileName,'第'+ str(i) + '条测试数据读取完成')
        url = url + api_host    #拼接ip和路径,组成请求链接
        data = data.split('~')      #转化为字典

        if method == "get":
            get_TestData(link=url,data=parameters)
def get_TestData(link,data):
    data = 
    link = 
    try:
        r = requests.get(lnk,timeout=1)
    except requests.exceptions.ConnectTimeout:
        log.writeLog(fileName,"请求超时")  
        exit()
    else:
        log.writeLog(fileName,"请求成功")  