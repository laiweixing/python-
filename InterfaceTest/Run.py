# -*- coding:utf-8 -*-

'''
小格兰特执行用例的文件
'''

import Core
import yaml

# 导入配置文件
yaml_name = "./estronger.yaml"
file_yaml = open(yaml_name, encoding='utf-8')
config = yaml.load(file_yaml)


if __name__ == '__main__':
    user = "小格兰特"
    # 示例
    Core.runTest('TestCase000.xlsx', config)
