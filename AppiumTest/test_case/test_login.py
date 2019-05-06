#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
登录页面自动化测试脚本
"""

from test_case.myunit import startEnd
from page_object.loginView import LoginView
from logs.loger import logging
import unittest


class TestLogin(startEnd):

    def test_login_right(self):
        logging.info('======测试正确登录======')
        login = LoginView(self.driver)
        login.login_action('bryce123', '74505208vv')

    def test_login_error(self):
        logging.info('======测试密码错误登录======')
        login = LoginView(self.driver)
        login.login_action('bryce123', '74505208')


if __name__ == '__main__':
    unittest.main()
