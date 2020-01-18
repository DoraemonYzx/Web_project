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
from selenium.webdriver.common.alert import Alert


class BaseAction:
    def __init__(self, _driver):
        self.driver = _driver
        self.timeout = 5
        self.t = 0.5

    def find_element(self, locator):
        """
        定位元素
        :param locator:
        :return: ele
        """
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("xpath", "value")')
        else:
            print('正在定位元素信息，定位方式-> %s ，value值-> %s' % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            print(ele)
            return ele

    def find_element_new(self, locator):
        """
        定位元素
        :param locator: 定位器
        :return: ele
        """
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("xpath", "value")')
        else:
            print('正在定位元素信息，定位方式-> %s ，value值-> %s' % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
            print(ele)
            return ele

    def send_keys(self, locator, keys):
        """
        在元素中输入内容
        :param locator: 定位器
        :param keys: 需要输入的内容
        :return:
        """
        ele = self.find_element(locator)
        ele.clear()
        try:
            ele.send_keys(keys)
            print("输入内容为-> %s" % keys)
        except BaseException:
            print("输入失败")

    def click(self, locator):
        """
        单击元素
        :param locator:  定位器
        :return:
        """
        ele = self.find_element(locator)
        try:
            ele.click()
            print("元素单击成功")
        except BaseException:
            print("元素单击失败")

    def is_url(self, _url):
        """
        返回bool类型，判断网址是否符合预期,网址结尾需要多加一个“/” 否则不匹配
        :param _url: 预期的网址
        :return: Ture or False
        """
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.url_to_be(_url))
            print("True 网址->%s 符合预期" % _url)
            return result
        except BaseException:
            print("False 网址->%s 不符合预期" % _url)
            return False

    def is_url_contains(self, _url):
        """
        返回bool类型，判断网址是否包含预期
        :param _url: 预期的网址
        :return: Ture or False
        """
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.url_contains(_url))
            print("True 网址->%s 包含预期" % _url)
            return result
        except BaseException:
            print("False 网址->%s 不包含预期" % _url)
            return False

    def is_title(self, _title):
        """
        返回bool类型，判断标题是否符合预期
        :param _title: 预期的标题
        :return: Ture or False
        """
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            print("True 标题->%s 符合预期" % _title)
            return result
        except BaseException:
            print("False 标题->%s 不符合预期" % _title)
            return False

    def is_title_contains(self, _title):
        """
        返回bool类型，判断标题是否包含预期
        :param _title:  预期的标题部分内容
        :return:  True or False
        """
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            print("True 标题->%s 包含预期" % _title)
            return result
        except BaseException:
            print("False 标题->%s 不包含预期" % _title)
            return False

    def is_text_in_element(self, locator, _text):
        """
        返回bool类型，判断元素文本内容是否符合预期
        :param locator:  定位器
        :param _text:  预期的文本内容
        :return:  True or False
        """
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            print("True 元素文本内容->%s 符合预期" % _text)
            return result
        except BaseException:
            print("Flase 元素文本内容->%s 不符合预期" % _text)
            return False

    def is_value_in_element(self, locator, _value):
        """
        返回bool类型，判断元素value值是否符合预期，value为空字符串，返回False
        :param locator:  定位器
        :param _value:  元素的value值
        :return:  True or False
        """
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
            print("True 元素value值->%s 符合预期" % _value)
            return result
        except BaseException:
            print("False 元素value值->%s 与预期不符" % _value)
            return False

    def is_alert(self):
        """
        判断是否有alert弹出，有则返回alert对象
        :return:  alert or False
        """
        try:
            _alert = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            print("True 找到alert弹窗")
            return _alert
        except BaseException:
            print("False 没有找到alert弹窗")
            return False

    def is_selected_locator(self, locator):
        """
        返回bool类型，判断select是否被勾选
        :param locator: 定位器
        :return: True or False
        """
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.element_located_to_be_selected(locator))
            print("True 对应select已被选中")
            return result
        except BaseException:
            print("False 对应select没有被选中")
            return False

    def is_element_exist(self, locator):
        """
        返回bool类型，判断元素是否存在
        :param locator:  定位器
        :return:  True or False
        """
        try:
            self.find_element(locator)
            print("元素存在于dom")
            return True
        except BaseException:
            print("元素不存在于dom")
            return False


if __name__ == "__main__":
    loc1 = ("id", "kw")
    loc2 = ("id", "su")
    loc3 = ("name", "tj_trnews")
    loc4 = ("link text", "搜索设置")
    loc5 = ("link text", "保存设置")
    loc6 = ("link text", "设置")
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.maximize_window()
    url = driver.current_url
    print(url)
    ba = BaseAction(driver)
    ba.is_url("www.baidu.com")
    ba.is_url("https://www.baidu.com/")
    ba.is_url_contains("1")
    ba.is_url_contains("www")
    ba.is_title("百度一下，你就121知道")
    ba.is_title("百度一下，你就知道")
    ba.is_title_contains("xxx")
    ba.is_title_contains("百度一下")
    ba.is_value_in_element(loc2, "ssssss")
    ba.is_value_in_element(loc2, "百度一下")
    ba.is_text_in_element(loc3, "xxx")
    ba.is_text_in_element(loc3, "新闻")
    ba.is_element_exist(loc1)
    ba.send_keys(loc1, 'woowowo')
    ba.click(loc2)
    ba.click(loc6)
    ba.click(loc4)
    ba.click(loc5)
    alert = ba.is_alert()
    print(alert.text)
    alert.accept()
    driver.quit()
