"""
======================
@author:多测师-黄sir
@time:2020/12/16:14:09
@email:hw18983616870@163.com
======================
"""
import unittest
from public.pages.BasePage import BasePage
from selenium import webdriver
from time import sleep
from public.utlis.ReadDataIni import *
from public.pages.Login_Element import Login_Element as le
class Test_Login(BasePage):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        BasePage.set_driver(cls.driver)

    def test01(self):
        driver = BasePage.get_driver()     #拿到BasePage模块的driver对象
        driver.get(url)
        driver.maximize_window()

        # 1.输入用户名

        BasePage.find_element(le.bbs_usern)
        BasePage.senkeys(username)
        sleep(1)
        # 2.输入密码

        BasePage.find_element(le.bbs_pwd)
        BasePage.senkeys(password)
        sleep(1)
        # 3.点击登录

        BasePage.find_element(le.bbs_loginbtn)
        BasePage.elem_click()
        # 4.断言
        sleep(4)

        value = BasePage.get_text(le.bbs_loginout)
        assert value == '退出'

if __name__ == '__main__':
    unittest.main()