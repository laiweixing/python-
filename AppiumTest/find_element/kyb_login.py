#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from find_element.capability import driver,NoSuchElementException

def login():
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("bryce123")

    driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("74505208vv")
    driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

try:
    drvier.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_myself").click()
except NoSuchElementException:
    login()
else:
    drvier.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_myself").click()
    drvier.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_username").click()
    login()

if __name__ == '__main__':
    print("ok")
