#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
登录功能测试
"""

import logging
import unittest

from businessView.loginView import LoginView
from common.myunit import startEnd


class TestLogin(startEnd):

    csv_file = '../data/data.csv'

    def test_login_right(self):
        logging.info('======测试正常登录======')
        lg = LoginView(self.driver)
        data = lg.get_csv_data(self.csv_file, 2)

        lg.login_action(data[0], data[1])
        self.assertTrue(lg.check_login_status())

    def test_login_error(self):
        logging.info('======测试密码错误登录======')
        lg = LoginView(self.driver)
        data = lg.get_csv_data(self.csv_file, 1)

        lg.login_action(data[0], data[1])
        self.assertFalse(lg.check_login_status())


if __name__ == '__main__':
    unittest.main()
