#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
注册模块封装
"""

import logging
import random

from common.common_fun import By, Common, NoSuchElementException
from common.desired_caps import appium_desired
from time import sleep


class RegisterView(Common):

    register_text = (By.ID, 'com.tal.kaoyan:id/login_register_text')

    # 头像设置相关元素
    userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    iv_picture = (By.ID, 'com.tal.kaoyan:id/iv_picture')
    picture_tv_ok = (By.ID, 'com.tal.kaoyan:id/picture_tv_ok')
    menu_crop = (By.ID, 'com.tal.kaoyan:id/menu_crop')

    # 完善资料界面元素
    perfectinfomation_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    major_subject_title = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    major_search_item_name = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')
    perfectinfomation_school = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_school')
    more_forum_title = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    university_search_item_name = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')
    perfectinfomation_goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

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

    # 完善个人资料
    def add_register_info(self):
        logging.info("======add_register_info======")

        logging.info("======select subject======")
        self.driver.find_element(*self.perfectinfomation_major).click()
        self.driver.find_elements(*self.major_subject_title)[0].click()
        self.driver.find_elements(*self.major_search_item_name)[8].click()

        logging.info("======select school======")
        self.driver.find_element(*self.perfectinfomation_school).click()
        a1 = 80/480
        b1 = 666/800
        a2 = 444/480
        b2 = 582/800
        x, y = self.get_size()
        self.driver.tap([(a1*x, b1*y)])
        self.driver.find_elements(*self.more_forum_title)[0].click()
        self.driver.find_elements(*self.university_search_item_name)[0].click()
        sleep(3)
        self.driver.tap([(a2*x, b2*y)])
        self.driver.find_element(*self.perfectinfomation_goBtn).click()

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
    password = '74505208vv'
    email = 'jackbryce' + str(random.randint(10000, 90000)) + '@163.com'
    register.register_action(username, password, email)
