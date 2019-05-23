#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import unittest
from time import sleep

from common.desired_caps import appium_desired


class startEnd(unittest.TestCase):

    def setUp(self):
        logging.info('======准备启动APP======')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('======准备关闭APP======')
        sleep(10)
        self.driver.close_app()
