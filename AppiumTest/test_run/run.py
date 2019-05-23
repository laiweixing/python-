#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
跑测试项
"""

import logging
import sys
import time
import unittest
from BSTestRunner import BSTestRunner

# # 指定项目文件的路径
path = 'E:\\project\\Test\\AppiumTest\\'
sys.path.append(path)

# 指定测试用例和测试报告的路径
test_dir = '../test_case'
report_dir = '../reports'

# 加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


# 定义报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + 'test_report.html'

# 运行用例并生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='Kyb Test Report', description='Kyb Android APP Test Report')
    logging.info("开始跑测试用例")
    runner.run(discover)
