"""
======================
@author:多测师-黄sir
@time:2020/12/16:11:11
@email:hw18983616870@163.com
======================
"""
'''此模块用来封装页面元素的所有操作方法'''
import unittest
# 以下两行代码为调制代码
# from selenium import webdriver
# driver =webdriver.Chrome()


class BasePage(unittest.TestCase):

    @classmethod
    def set_driver(cls,driver):     #单例模式
        cls.driver = driver        #定义一个打开浏览器的变量，并且定义成类的属性

    @classmethod
    def get_driver(cls):

        return cls.driver          #把设置的driver变量，通过返回方法返回给函数调用处
    baidu_input = ('id','kw')
    @classmethod
    def find_element(cls,element):
        type = element[0]
        value = element[1]
        if type == 'id':
            cls.elem = cls.driver.find_element_by_id(value)
        elif type == 'name':
            cls.elem = cls.driver.find_element_by_name(value)
        elif type == 'class':
            cls.elem = cls.driver.find_element_by_class_name(value)
        elif type == 'css':
            cls.elem = cls.driver.find_element_by_css_selector(value)
        elif type == 'link':
            cls.elem = cls.driver.find_element_by_link_text(value)
        elif type == 'xpath':
            cls.elem = cls.driver.find_element_by_xpath(value)
        return cls.elem

    '''封装点击页面元素的方法===》二次封装'''
    @classmethod
    def elem_click(cls):
        return cls.elem.click()
    '''封装输入内容的方法'''
    @classmethod
    def senkeys(cls,value):
        return cls.elem.send_keys(value)

    @classmethod
    def wait(cls,sec):
        return cls.driver.implicitly_wait(sec)

    @classmethod
    def switchhandle(cls):
        handles = cls.driver.window_handles
        cls.driver.switch_to.window(handles[-1])

    @classmethod
    def get_text(cls,element):
        return BasePage.find_element(element).text

    @classmethod
    def get_title(cls):
        return cls.driver.title

# if __name__ == '__main__':
    # b = BasePage()
    # b.set_driver(driver)
    # chrome1 = b.get_driver()
    # chrome1.get('http://www.baidu.com')

    # baidu_link = ('link','hao123')
    # b.find_element(baidu_link)
    # b.elem_click()
    # baidu_input = ('id','kw')
    # b.find_element(baidu_input)
    # b.senkeys('python')















