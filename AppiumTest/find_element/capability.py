#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from logs.loger import logging
import yaml
from os import path

yaml_name = "./config/kyb_caps.yaml"
file = open(yaml_name, 'r')
data = yaml.load(file)

desired_caps = {}
desired_caps['platformName'] = data['platformName']
desired_caps['platforVersion'] = data['platforVersion']
desired_caps['deviceName'] = data['deviceName']
# desired_caps['automationName'] = data['automationName']         # toast获取提示时需要打开

base_dir = path.dirname(path.dirname(__file__))
app_path = path.join(base_dir, 'app', data['appName'])
desired_caps['app'] = app_path

desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']

desired_caps['noReset'] = data['noReset']    # 数据清理
desired_caps['noSign'] = data['noSign']     # 再次签名
# sen_keys()传入中文配置
desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
desired_caps['resetKeyboard'] = data['resetKeyboard']

logging.info("------开始启动APP------")
driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
driver.implicitly_wait(30)      # 隐式等待
logging.info("------启动APP成功------")


def check_cancelBtn():
    logging.info("check cancelBtn")
    try:
        cancelBtn = driver.find_element_by_id("android:id/button2")
    except NoSuchElementException:
        logging.info("no cancelBtn")
    else:
        cancelBtn.click()


def check_skipBtn():
    logging.info("check skipBtn")
    try:
        skipBtn = driver.find_element_by_id("com.tal.kaoyan:id/tv_skip")
    except NoSuchElementException:
        logging.info("no skipBtn")
    else:
        skipBtn.click()


check_cancelBtn()
check_skipBtn()


if __name__ == '__main__':
    print("APP启动完成")
