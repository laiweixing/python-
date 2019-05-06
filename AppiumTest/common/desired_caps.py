#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
APP启动配置
"""

from appium import webdriver
import yaml
import logging
import logging.config
from os import path

CON_LOG = './config/log.conf'
log_file_path = path.abspath(path.join(path.abspath('.'), CON_LOG))
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()


def appium_desired():
    yaml_file = "./config/kyb_caps.yaml"
    with open(yaml_file, 'r', encoding='utf-8') as file:
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
    driver.implicitly_wait(20)      # 隐式等待
    logging.info("------启动APP成功------")
    return driver


if __name__ == '__main__':
    appium_desired()
