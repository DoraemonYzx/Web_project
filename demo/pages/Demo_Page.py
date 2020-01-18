from common.base_action import BaseAction
import unittest
import xlrd


class DemoPage(BaseAction):
    loc_input_user = ("id", "login_name")
    loc_input_pwd = ("id", "pwd")
    loc_login_btn = ("id", "btn_login")
    loc_login_name = ("id", "show_employeename")

    def __init__(self, _driver):
        super().__init__(_driver)

    def input_user(self, username):
        self.send_keys(self.loc_input_user, username)

    def input_pwd(self, pwd):
        self.send_keys(self.loc_input_pwd, pwd)

    def click_login_btn(self):
        self.click(self.loc_login_btn)

    def expect_login_name(self, expect):
        result = self.is_text_in_element(self.loc_login_name, expect)
        return result

    def get_login_text(self):
        text = self.find_element(self.loc_login_name).text
        return text

    def login(self, username, pwd):
        self.input_user(username)
        self.input_pwd(pwd)
        self.click_login_btn()

    # def read_excel(self):
    #     wb = xlrd.open_workbook("D:\\Web_project\\demo\\data.datas.xlsx")
    #     print(wb.sheet_names())
    #     # sheet_username = wb.sheet_by_name("username")
    #     # sheet_pwd = wb.sheet_by_name("pwd")
    #     # sheet_except = wb.sheet_by_name("except")
    #     # list_username = []
    #     # list_pwd = []
    #     # list_except = []
    #     # for i in range(sheet_username.nrows):
    #     #     list_username.append(sheet_username.row_values(0)[i])
    #     #
    #     # print(list_username)
