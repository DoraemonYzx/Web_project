#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: conftest.py
@time: 2020/01/21
"""
import pytest


"""使用装饰器标记fixture的功能
    可以使用此装饰器（带或不带参数）来定义fixture功能。 fixture功能的名称可以在以后使用
    引用它会在运行测试之前调用它：test模块或类可以使用pytest.mark.usefixtures（fixturename标记。 
    测试功能可以直接使用fixture名称作为输入参数，在这种情况下，夹具实例从fixture返回功能将被注入。

   :arg scope: scope 有四个级别参数 "function" (默认), "class", "module" or "session".

   :arg params: 一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它

   :arg autouse:  如果为True，则为所有测试激活fixture func 可以看到它。 如果为False（默认值）则显式需要参考来激活fixture

   :arg ids: 每个字符串id的列表，每个字符串对应于params 这样他们就是测试ID的一部分。 如果没有提供ID它们将从params自动生成

   :arg name: fixture的名称。 这默认为装饰函数的名称。 如果fixture在定义它的同一模块中使用，夹具的功能名称将被请求夹具的功能arg遮蔽; 
              解决这个问题的一种方法是将装饰函数命名 “fixture_ <fixturename>”然后使用“@ pytest.fixture（name ='<fixturename>'）”。
"""

"""
fixture作用范围
fixture里面有个scope参数可以控制fixture的作用范围:session > module > class > function
- function 每一个函数或方法都会调用
- class  每一个类调用一次，一个类可以有多个方法
- module，每一个.py文件调用一次，该文件内又有多个function和class
- session 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
"""

"""
fixture 写在conftest.py文件中供用例调用，调用时，不用import conftest ,
"""


@pytest.fixture(scope="class")
def login():
    print("输入账号，密码先登录")


@pytest.fixture()
def text1():
    print("退出")


@pytest.fixture()
def text2():
    print("退出2")