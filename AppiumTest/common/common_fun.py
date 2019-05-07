#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
封装一些公共类
"""

import os
import time

from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from logs.loger import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Common(BaseView):

    cancelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    wemedia_cancle = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cancel')

    # 检测启动页跳过按钮
    def check_cancelBtn(self):
        logging.info("======check cancelBtn======")
        try:
            element = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info("======no cancelBtn======")
        else:
            logging.info("======close cancelBtn======")
            element.click()

    # 检测升级弹窗
    def check_skipBtn(self):
        logging.info("======check skipBtn======")
        try:
            element = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info("======no skipBtn======")
        else:
            logging.info("======close skipBtn======")
            element.click()

    # 检测广告弹窗
    def check_market_ad(self):
        logging.info("======check market_ad======")
        try:
            element = self.driver.find_element(*self.wemedia_cancle)
        except NoSuchElementException:
            logging.info("======no market_ad======")
        else:
            logging.info("======close market_ad======")
            element.click()

    # 获取屏幕尺寸
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向左滑动
    def swipeLeft(self):
        logging.info('======swipe_left======')
        lt = self.get_size()
        x1 = int(lt[0] * 0.9)
        y1 = int(lt[1] * 0.5)
        x2 = int(lt[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 2000)

    # 获取当前时间
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H-%M-%S")
        return self.now

    # 截图
    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_cancelBtn()
    # com.check_skipBtn()
    com.swipeLeft()
    com.getScreenShot('startAPP')
