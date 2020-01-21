from common.base_action import BaseAction
from common.base_driver import BaseDriver
from pages.Demo_Page import DemoPage
# import unittest
import pytest
from selenium import webdriver
from common.read_excel import ReadExcel
import os


# @pytest.fixture(scope="class")
# def login():
#     print("输入账号，密码先登录")
#
#
# @pytest.fixture()
# def text1():
#     print("退出")
#
#
# @pytest.fixture()
# def text2():
#     print("退出2")
"""
    pytest经典案例
    @pytest.mark.parametrize("user,pwd,expect", [["admin", "123", "1"], ["tom", "321", "1"], ["kitty", "000", "1"], ])
    在这里，@parametrize装饰器定义了三个不同的(user,pwd,expect) 元组，以便该test_02函数依次使用它们运行三次
    @pytest.mark.parametrize需要定义在需要使用数据的用例上方
"""


class TestCase():
    def test_01(self, login):
        """测试1"""
        print("测试用例1")

    @pytest.mark.parametrize("user,pwd,expect", [["admin", "123", "1"], ["tom", "321", "1"], ["kitty", "000", "1"], ])
    def test_02(self, text1, text2, user, pwd, expect):
        """测试2"""
        print("测试用例2")
        print(user, pwd, expect)

    def test_03(self, login):
        """测试2"""
        print("测试用例3")


# @pytest.fixture(scope="class")
# def first():
#     print("\n获取用户名，scope为class级别只运行一次")
#     a = "nuo"
#     return a
#
#
# class TestCase():
#     def test_1(self,first):
#         '用例传fixture'
#         print("测试账号：%s"%first)
#         assert first == "nuo"
#
#     def test_2(self,first):
#         '用例传fixture'
#         print("测试账号：%s"%first)
#         assert first == "nuo"
if __name__ == "__main__":
    pytest.main(["-s", "test_demo_pytest1.py"])
