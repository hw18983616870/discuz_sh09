"""
======================
@author:多测师-黄sir
@time:2020/12/16:10:01
@email:hw18983616870@163.com
======================
"""
'''
此模块用来读取data包内的ini文件的所有内容
configparser --》用于读取ini文件内容的模块
'''
from configparser import ConfigParser
from config.Config import *
class ReadDataIni(ConfigParser):

    def __init__(self,filename):
        super(ConfigParser, self).__init__()       #继承父类的构造函数
        self.read(filename)    #调用ConfigParser类中的read()方法，用来读取文件

    '''定义一个获取文件内的参数信息的方法'''
    def read_data(self,section=None,option=None):
        return self.get(section,option)

ini_path = os.path.join(data_path,'Data.ini')
# print(ini_path)
r = ReadDataIni(ini_path)
url = r.read_data(section='test_data',option='url')
# print(url)                # http://192.168.22.130/bbs
username = r.read_data(section='test_data',option='username')
# print(username)           # admin

password = r.read_data(section='test_data',option='pwd')
# print(password)           # 123456










