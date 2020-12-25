"""
======================
@author:多测师-黄sir
@time:2020/12/16:15:43
@email:hw18983616870@163.com
======================
"""
from time import sleep
from public.pages.BasePage import BasePage
from public.pages.Manage_Element import Manage_Element as me
class Test_Manage_Center(BasePage):

    def test01(self):
        # 点击管理中心
        BasePage.find_element(me.manage_center)
        BasePage.elem_click()
        BasePage.switchhandle()
        sleep(5)
        #断言页面打开，且切换成功
        value = BasePage.get_text(me.manage_center1)
        assert value =='腾讯云'