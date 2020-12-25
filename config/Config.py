"""
======================
@author:多测师-黄sir
@time:2020/12/16:9:32
@email:hw18983616870@163.com
======================
"""
''''此模块用来存放当前项目的所有文件和目录的绝对路径'''
import os

# 1.当前项目的绝对路径
path = os.path.dirname(os.path.dirname(__file__))   #获取当前目录的上一级目录的绝对路径
# print(path)    # D:/workspace/discuz_sh09

# 2.config目录的绝对路径
config_path = os.path.join(path,'config')
# print(config_path)   # D:/workspace/discuz_sh09\config

# 3.data目录的绝对路径
data_path = os.path.join(path,'data')

# 4.pages目录的绝对路径
pages_path = os.path.join(path,'public','pages')

# 5.utlis目录的绝对路径
utlis_path = os.path.join(path,'public','utlis')

# 6.report目录的绝对路径
report_path = os.path.join(path,'report')

# 7.testcase目录的绝对路径
testcase_path = os.path.join(path,'testcase')
















