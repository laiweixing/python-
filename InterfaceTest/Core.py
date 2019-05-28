#!/usr/bin/python
# -*- coding: utf-8 -*-

# Todo：接口自动化测试
# Author：Bryce

"""
核心模块
主逻辑：获取测试用例数据、发送接口请求、比对返回数据、分析测试结果
时间：2019-3-21
暂未考虑加密请求，后续添加
"""

# 引入第三方库
import os
# import re
import sys
import json
import xlrd
import requests
from enum import Enum
# from urllib.parse import quote

# 引入封装模块
import Common
import ReportHtml
import Log
# import ExcelHelper.modifyExcel


# 定义全局变量
data = []   # 定义一个变量data用于存储返回的的数据集


class serverType(Enum):     # 枚举服务器类型
    test = 1    # 测试服
    formal = 2  # 正式服


# 获取测试数据并执行用例
def runTest(testCaseFile, config):
    fileName = testCaseFile     # 日志文件名
    Log.resetLogFile(fileName)      # 重置日志文件内容
    Log.writeLog(fileName, '---------------------------------------------')
    Log.writeLog(fileName, '准备执行测试用例')

    testCaseFile = os.path.join(Common.gCurDir + '\\TestCase', testCaseFile)    # 获取用例文件路径
    if not os.path.exists(testCaseFile):
        Log.writeLog(fileName, '测试用例文件不存在！！！')
        sys.exit()

    ipType = config['ipType']
    url = config['url']
    # encryption = config['encryption']
    rcode = config['code']
    rdesc = config['desc']
    rdata = config['data']
    rcode_value = config['code_value']

    testCase = xlrd.open_workbook(testCaseFile)
    table = testCase.sheet_by_index(0)
    Log.writeLog(fileName, '准备加载excel用例数据')

    for i in range(1, table.nrows):
        if table.cell(i, 8).value == 'Yes' or table.cell(i, 8).value == 'yes':
            Log.writeLog(fileName, '第'+str(i)+'行开始执行了')
        else:
            continue    # 如果第八行的数据不等于Yes或yes就跳过执行下一个用例

        num = int(table.cell(i, 0).value)      # 获取用例编号
        api_title = Common.delEnter(table.cell(i, 1).value)     # 获取测试目的
        api_host = Common.delEnter(table.cell(i, 2).value)       # 获取接口地址路径
        method = Common.delEnter(table.cell(i, 3).value)     # 获取请求类型
        parameters = Common.delEnter(table.cell(i, 4).value)        # 获取传入参数及值
        returnVal = Common.delEnter(table.cell(i, 5).value)         # 判断是否有返回值
        # data_type = Common.delEnter(table.cell(i, 6).value)        # 获取预期返回的数据类型
        check_data = Common.delEnter(table.cell(i, 7).value)          # 获取预期返回的数据：参数

        Log.writeLog(fileName, '第' + str(i) + '条测试数据读取完成')
        url = url + api_host    # 拼接ip和路径,组成请求链接
        check_data = check_data.split('~')      # 预期返回数据转化为字典
        headers = {'Content-Type': "application/x-www-form-urlencoded"}     # post请求头内容
        results = ''    # 分析结果
        rResult = ''    # 定义一个变量rResult,用于判断result中key是否完整

        # 测试服（生产环境）
        if ipType == serverType.test.value:
            # get请求后续补充，目前都是post请求
            if method == "get":
                parameters = Common.change_parameters(parameters)
                url = url + parameters
                get_TestData(lnk=url, fileName=fileName)
            elif method == "post":
                parameters = eval(parameters)
                post_TestData(lnk=url, json=parameters, headers=headers, fileName=fileName)

            response_time = response.elapsed.total_seconds()        # 响应时间
            state = response.status_code        # 请求状态码
            if state == 200:
                Log.writeLog(fileName, '测试服接口请求成功')
            else:
                Log.writeLog(fileName, '测试服接口请求失败,执行下一条数据')
                continue
            rContent = json.loads(response.text)        # 解析json格式数据

            rCode = rContent[rcode]     # 错误码
            rDesc = rContent[rdesc]     # 错误描述

            rResultFlg = True
            # 判断是否有返回值
            if returnVal == '返回值=y' and rCode == rcode_value:
                rData = rContent[rdata]     # 接口返回的json数据
                # 判断返回值是否有result
                if len(rContent) < 3 or rData == '':
                    results = "没有result参数返回，检查是否真的有返回值"
                else:
                    rResult = rData

                    # 首先，判断result是否为空
                    if len(rResult) == 0:
                        results = "result值为空"
                    else:
                        # 判断返回的数据是否为字符串
                        if isinstance(rResult, str):
                            try:
                                rResult = eval(rResult)     # 字符串转化为字典
                            except Exception as e:
                                print(e)
                                Log.writeLog(fileName, "第" + str(i) + "条数据，转换出错了，检查返回的数据类型")
                            else:
                                Log.writeLog(fileName, "第" + str(i) + "数据转换成功")
                        # 判断返回的数据是否为列表
                        elif isinstance(rResult, list):
                            flg = True
                            # 用预期结果比对返回数据
                            for key1 in check_data:
                                if key1 not in rResult:
                                    results = "result中没有返回"+str(key1)
                                    flg = False
                            # 用返回数据比对预期结果
                            for key2 in rResult:
                                if key2 not in check_data:
                                    results = "result中多返回了"+str(key2)
                                    flg = False
                            if flg is True:
                                results = "result返回完整"
                        # 判断返回的数据是否为字典
                        elif isinstance(rResult, dict):
                            # 判断result长度是否为1
                            if len(rResult) == 1:
                                flg = True
                                # 判断返回的result中key与value是否完整
                                for key in check_data:
                                    if key not in rResult[0].keys():
                                        results = "result中没有返回"+str(key)
                                        flg = False
                                for key, value in rResult[0].items():
                                    if value == '':
                                        results = "result中"+str(key)+"的值为空"
                                        flg = False
                                    # value为整数或小数时
                                    elif type(value) is int or type(value) is float:
                                        if value < 0:
                                            results += "result中"+str(key)+"的值为负数"
                                            flg = False
                                    # value为字典时
                                    elif isinstance(value, list):
                                        results = "result中"+str(key)+"的值较复杂，请参照接口文档仔细比对"
                                        flg = False
                                if flg is True:
                                    results = "result返回完整"
                            # 判断result长度是否为大于1
                            elif len(rResult) > 1:
                                flg = True
                                # 判断返回的result中key与value是否完整
                                for key in check_data:
                                    if key not in rResult.keys():
                                        results = "result中没有返回"+str(key)
                                        flg = False
                                for key, value in rResult.items():
                                    if value == '':
                                        results = "result中"+str(key)+"的值为空"
                                        flg = False
                                    # value为整数或小数时
                                    elif type(value) is int or type(value) is float:
                                        if value < 0:
                                            results = "result中"+str(key)+"的值为负数"
                                            flg = False
                                    # value为字典时
                                    elif isinstance(value, list):
                                        results = "result中"+str(key)+"的值较复杂，请参照接口文档仔细比对"
                                        flg = False
                                if flg is True:
                                    results = "result返回完整"
                                Log.writeLog(fileName, "result返回了多个列表")
                        else:
                            Log.writeLog(fileName, "rResult的数据类型为：" + type(rResult))

            elif returnVal == '返回值=y' and rCode != rcode_value:
                results = 'code:'+str(rCode)+' '+'desc:'+str(rDesc)

            elif returnVal == '返回值=n' and rCode == rcode_value:
                results = '数据返回成功'

            elif returnVal == '返回值=n' and rCode != rcode_value:
                results = 'code:'+str(rCode)+' '+'desc:'+str(rDesc)

        # 正式服（线上环境）
        elif ipType == serverType.formal.value:
            print("待添加")

        # 把需要显示在html上的数据写入一个集合
        if rResultFlg is False:
            rResult = '无返回值'
            data.append(
                (
                    num,    # 序号
                    api_title,  # 标题
                    api_host,    # 请求接口地址
                    state,  # 状态码
                    rCode,
                    rDesc,
                    rResult,
                    results,    # 分析结果
                    response_time   # 响应时间
                    )
                )
        else:
            data.append(
                (
                    num,    # 序号
                    api_title,  # 标题
                    api_host,   # 请求接口地址
                    state,  # 状态码
                    rCode,
                    rDesc,
                    rResult,
                    results,    # 分析结果
                    response_time,  # 响应时间
                )
            )
        # elif ipType == serverType.formal.value:
            # if method == "get":
            # 需确认加密算法，暂不开发

    # 生成本地html报告
    ReportHtml.CreateReportHtml(data, fileName)


# Get请求函数
def get_TestData(lnk, fileName):
    try:
        global response
        response = requests.get(lnk, timeout=1)
    except requests.exceptions.ConnectTimeout:
        Log.writeLog(fileName, "请求超时")
        sys.exit()
    else:
        Log.writeLog(fileName, "请求成功")
        return response


# Post请求函数
def post_TestData(lnk, json, headers, fileName):
    try:
        global response
        response = requests.post(lnk, json, headers)
    except requests.exceptions.ConnectTimeout:
        Log.writeLog(fileName, '服务器连接超时了，请确认服务器是否打开')
        sys.exit()
    else:
        return response
