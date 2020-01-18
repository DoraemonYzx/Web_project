#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: base_driver.py
@time: 2020/01/10
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:

    # def base_driver_chrome():
    #     _driver = webdriver.Chrome()
    #     return _driver
    #
    #
    # def base_driver_firefox():
    #     _driver = webdriver.Firefox()
    #     return _driver
    #
    #
    # def open_bow(_driver, url="http://www.baidu.com"):
    #     _driver.get(url)
    def __init__(self, driver):
        self.driver = driver
        # self.base_url = "www.baidu.com"

    def open(self, driver):
        print("……………………用例开始……………………")
        self.driver.maximize_window()
        print("………………清空浏览器缓冲中………………")
        self.driver.delete_all_cookies()
        print("………………刷新浏览器中………………")
        self.driver.refresh()


# if __name__ == "__main__":
#     pass