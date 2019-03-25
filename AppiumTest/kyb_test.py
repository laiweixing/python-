#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    这是一个简单的示例 自动化脚本
"""
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:62025'
desired_caps['platforVersion']='5.1.1'

desired_caps['app']=r'C:\\Users\\user\\Downloads\\APK\\kaoyanbang.apk'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

# desired_caps['automationName'] = 'uiautomator2'         #toast获取提示时需要打开
# desired_caps['noReset'] = 'True'         #重置会话信息 ps:默认重置 True 不重置

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)      #隐式等待

# driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_userheader").click()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("bryce123")
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("74505208vv")
driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()



