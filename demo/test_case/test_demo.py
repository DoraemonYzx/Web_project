from common.base_action import BaseAction
from common.base_driver import BaseDriver
from pages.Demo_Page import DemoPage
import unittest
import ddt
from selenium import webdriver
from common.read_excel import ReadExcel
import os
# 测试数据1
testdates1 = [
                {"username": "YG3346", "password": "654321", "expect": "余振新"},
                {"username": "YG0000", "password": "000000", "expect": "余振新"},
                {"username": "YG3346", "password": "654321", "expect": "余振新"},
             ]
# 测试数据2
testdates2 = [
                {"username": "YG3346", "password": "654321", "expect": "余振新", "result": True},
                {"username": "YG0000", "password": "000000", "expect": "余振新", "result": False},
                {"username": "YG3346", "password": "654321", "expect": "余振新", "result": False},
             ]
# 读取excel
# fliepath = r"D:\Web_project\demo\data\datas.xlsx"

propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath = os.path.join(propath, "data", "datas.xlsx")

sheetName = "Sheet1"
data = ReadExcel(filepath, sheetName)
print(data.dict_data())

url = "http://180.106.83.239:18080/login.html"

"""
测试数据驱动：
test_01: 输入账号密码后点击登录，获取登录名，判断登录名是否符合预期来断言是否登录成功
        （登录失败会有弹窗，无法进入登录成功后的页面，定位登录名会抛出TimeOut异常，实际用例执行成功，但用例会执行失败）
test_02: 输入账号密码后点击登录，获取登录名，判断登录名是否符合预期来断言是否登录成功
        （在测试数据增加“result”字段，赋值True or False，
          调用common方法返回预期与实际为True or False后，与“result”断言，解决没有获取到登录名会使用例失败的问题）
"""


@ddt.ddt
class TestDemo(unittest.TestCase):
    """使用数据驱动测试登录功能"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_driver = BaseDriver(cls.driver)
        cls.demo_page = DemoPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(url)
        self.base_driver.open(url)

    # 供test_01使用的封装登录方法
    def login_case1(self, username, pwd, expect):
        self.demo_page.login(username, pwd)
        result = self.demo_page.get_login_text()
        print("预期结果为：-> %s ,实际结果为：-> %s" % (expect, result))
        self.assertTrue(result == expect)

    # 供test_02使用的封装登录方法
    def login_case2(self, username, pwd, expect, _result):
        self.demo_page.login(username, pwd)
        result = self.demo_page.expect_login_name(expect)
        print("预期结果为：-> %s ,实际结果为：-> %s" % (_result, result))
        self.assertTrue(result == _result)

    @ddt.data(*testdates1)
    def test_01(self, data):
        """测试1"""
        print("测试数据: %s " % data)
        self.login_case1(data["username"], data["password"], data["expect"])

    @ddt.data(*testdates2)
    def test_02(self, data):
        """测试2"""
        print("测试数据: %s " % data)
        self.login_case2(data["username"], data["password"], data["expect"], data["result"])

    # def test_02(self):
    #     data = testdates[1]
    #     # print(data)
    #     # print(data["username"])
    #     # self.dp.input_user(data["username"])
    #     # self.dp.input_user(data["psd"])
    #     self.demo_page.input_user(data["username"])
    #     self.demo_page.input_pwd(data["password"])
    #     self.demo_page.click_login_btn()
    #     result = self.demo_page.expect_login_name(data["expect"])
    #     self.assertTrue(result)
    #
    # def test_03(self):
    #     data = testdates[2]
    #     # print(data)
    #     # print(data["username"])
    #     # self.dp.input_user(data["username"])
    #     # self.dp.input_user(data["psd"])
    #     self.demo_page.input_user(data["username"])
    #     self.demo_page.input_pwd(data["password"])
    #     self.demo_page.click_login_btn()
    #     result = self.demo_page.expect_login_name(data["expect"])
    #     self.assertTrue(result)

    # def test_03(self):
    #     self.demo_page.read_excel()


if __name__ == "__main__":
    unittest.main()
