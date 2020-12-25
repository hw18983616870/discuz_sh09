"""
======================
@author:多测师-黄sir
@time:2020/12/16:15:09
@email:hw18983616870@163.com
======================
"""
'''
此模块用于存放登录页面的元素定位
po设计  page object 页面对象设计方法 
把页面元素的属性封装成类的属性，再调用
优点：
1.很大程度的提高了代码的复用性
2.把测试用例中的相关代码进行解耦
3.增强了代码健壮性
缺点：
代码量增加
'''
class Login_Element:
    # 1.用户名输入框
    bbs_usern = ('id', 'ls_username')
    # 2.密码输入框
    bbs_pwd = ('id', 'ls_password')
    # 3.登录按钮
    bbs_loginbtn = ('class', 'pn')
    # 4.退出按钮
    bbs_loginout = ('xpath', '//*[@id="um"]/p[1]/a[7]')