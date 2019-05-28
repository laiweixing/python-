#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
注册功能测试
"""

import logging
import random
import unittest

from businessView.registerView import RegisterView
from common.myunit import startEnd


class TestRegister(startEnd):

    def test_register_right(self):
        logging.info("======测试正常注册======")
        rg = RegisterView(self.driver)

        username = "bryce" + 'lwx' + str(random.randint(10000, 90000))
        password = '74505208Xvv'
        email = 'jackbryce' + str(random.randint(10000, 90000)) + '@163.com'

        rg.register_action(username, password, email)
        rg.add_register_info()
        self.assertTrue(rg.check_register_status())

    def test_register_error(self):
        logging.info("======测试异常注册 密码为空======")
        rg = RegisterView(self.driver)

        username = "bryce" + 'lwx' + str(random.randint(10000, 90000))
        password = ''
        email = 'jackbryce' + str(random.randint(10000, 90000)) + '@163.com'

        rg.register_action(username, password, email)
        rg.add_register_info()
        self.assertTrue(rg.check_register_status())


if __name__ == '__main__':
    unittest.main()
