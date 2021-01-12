"""
======================
@author:多测师-黄sir
@time:2020/12/16:15:46
@email:hw18983616870@163.com
======================
"""
'''此模块用运行所有的测试用例'''
import unittest
from public.utlis.HTMLTestRunner3_New import HTMLTestRunner
from config.Config import *
import time
from public.utlis.mail3 import SendMail
def run_all():

    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path,pattern='Test*.py')
    # print(discover)
    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    filename = report_path+'ui_report.html'
    f = open(file=filename,mode='wb')
    runner = HTMLTestRunner(stream=f,
                            title='DISCUZ论坛UI自动化测试报告',
                            description='用例执行情况如下：',
                            tester='多测师黄sir')
    runner.run(discover)
    f.close()
    sm = SendMail(send_msg=filename,attachment=filename)
    sm.send_mail()
run_all()


