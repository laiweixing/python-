#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from common.desired_caps import appium_desired
from logs.loger import logging
from time import sleep


class startEnd(unittest.TestCase):

    def setUp(self):
        logging.info('======setUp======')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('======tearDown======')
        sleep(10)
        self.driver.close_app()
