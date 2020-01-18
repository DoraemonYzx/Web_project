#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: read_yaml.py
@time: 2020/01/16
"""
import yaml

f1 = '''
---
name: James
age: 20
---
name: Lily
age: 19
'''

aproject = {'name': 'Silenthand Olleander',
            'race': 'Human',
            'traits': ['ONE_HAND', 'ONE_EYE']
            }


obj1 = {"name": "James", "age": 20}
obj2 = ["Lily", 19]


class ReadYaml:

    @staticmethod
    def read_yaml():
        """
        load(f)读取f返回的yaml文件
        用f接受返回一个yaml对象
        """
        with open(r'D:\Web_project\demo\data\config_test.yml', encoding='utf-8') as f:
            y = yaml.load(f, Loader=yaml.FullLoader)
            print(y)

    @staticmethod
    def read_yaml_all():
        """
        load_all()生成一个迭代器
        如果string或文件包含几块yaml文档，你可以使用yaml.load_all来解析全部的文档
        """
        # f = open(r'D:\Web_project\demo\data\config_test.yml')
        y = yaml.load_all(f1, Loader=yaml.FullLoader)
        for data in y:
            print(data)

    @staticmethod
    def read_yaml_dump():
        """
        dump(aproject,f)
        第一个参数：将python格式数据aproject改成yaml格式
        第二个参数：将转换后的yaml格式写入打开的yaml对象f中，非必填
        """
        print(yaml.dump(aproject))

    @staticmethod
    def read_yaml_dymp_all():
        """
        dump_all([obj1,obj2],f)
        第一个参数：用列表将多个python格式数据改成yaml格式
        第二个参数：将转换后的yaml格式写入打开的yaml对象f中，非必填

        """
        with open(r'E:\AutomaticTest\Test_Framework\config\config.yml', 'w') as f:
            yaml.dump_all([obj1, obj2], f)

    @staticmethod
    def read_yaml_list():
        """
        用list获取load_all,通过下标选择需要获取的yaml
        """
        with open(r'D:\Web_project\demo\data\config_test.yml', encoding='utf-8') as file:
            y = list(yaml.load_all(file, Loader=yaml.FullLoader))
            print(y[0])
            # print(y[1])


if __name__ == "__main__":
    readyaml = ReadYaml()
    # readyaml.read_yaml()
    # readyaml.read_yaml_all()
    # readyaml.read_yaml_dump()
    # readyaml.read_yaml_list()
