#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
注册模块封装
"""

import random

from common.common_fun import By, Common, NoSuchElementException
from common.desired_caps import appium_desired
from logs.loger import logging


class RegisterView(Common):

    register_text = (By.ID, 'com.tal.kaoyan:id/login_register_text')

    # 头像设置相关元素
    userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    iv_picture = (By.ID, 'com.tal.kaoyan:id/iv_picture')
    picture_tv_ok = (By.ID, 'com.tal.kaoyan:id/picture_tv_ok')
    menu_crop = (By.ID, 'com.tal.kaoyan:id/menu_crop')

    # 用户名、密码、邮箱相关元素
    register_username = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_btn = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')

    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

    # 注册步骤
    def register_action(self, register_username, register_password, register_email):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info("======register_action======")
        self.driver.find_element(*self.register_text).click()

        self.driver.find_element(*self.userheader).click()
        logging.info("======set userheader======")
        self.driver.find_elements(*self.iv_picture)[1].click()
        self.driver.find_element(*self.picture_tv_ok).click()
        self.driver.find_element(*self.menu_crop).click()

        logging.info("register_username is %s" % register_username)
        self.driver.find_element(*self.register_username).send_keys(register_username)

        logging.info("register_password is %s" % register_password)
        self.driver.find_element(*self.register_password).send_keys(register_password)

        logging.info("register_email is %s" % register_email)
        self.driver.find_element(*self.register_email).send_keys(register_email)

        self.driver.find_element(*self.register_btn).click()

    # 检测注册状态
    def check_register_status(self):
        logging.info("======check_register_status======")
        self.check_market_ad()

        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error("register fail!")
            self.getScreenShot("register fail")
            return False
        else:
            logging.info("register success!")
            return True


if __name__ == '__main__':
    driver = appium_desired()
    register = RegisterView(driver)
    username = "bryce" + 'lwx' + str(random.randint(10000, 90000))
    email = 'jackbryce' + str(random.randint(10000, 90000)) + '@163.com'
    register.register_action(username, '74505208vv', email)
    register.check_register_status()
