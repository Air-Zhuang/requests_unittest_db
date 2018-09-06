#coding:utf-8
import unittest
import requests
import os,sys
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class AddEventTest(object):
    '''添加发布会'''
    def __init__(self):
        self.base_url="http://127.0.0.1:8000/api/add_event/"
    def test_add_event_all_null(self):
        '''所有参数为空'''
        payload={'eid':'','':'','limit':'','address':'','start_time':''}
        r=requests.post(self.base_url,data=payload)
        result=r.json()
        print(result)
    def test_add_event_eid_exist(self):
        '''id已经存在'''
        payload = {'eid': '1', 'name': '一加4发布会', 'limit': '2000', 'address': '深圳宝体', 'start_time': '2017'}
        r=requests.post(self.base_url,data=payload)
        result=r.json()
        print(result)
    def test_add_event_name_exist(self):
        '''名称已经存在'''
        payload = {'eid': '11', 'name': '红米Pro发布会', 'limit': '2000', 'address': '深圳宝体', 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
    def test_add_event_data_type_error(self):
        '''日期格式错误'''
        payload = {'eid': '11', 'name': '一加4手机发布会', 'limit': '2000', 'address': '深圳宝体', 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
    def test_add_event_success(self):
        '''添加成功'''
        payload = {'eid': '11', 'name': '一加4手机发布会', 'limit': '2000', 'address': '深圳宝体',
                   'start_time': '2019-08-20 00:25:42'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
if __name__ == '__main__':
    test_data.init_data()#初始化测试数据
    test=AddEventTest()
    test.test_add_event_all_null()
    test.test_add_event_eid_exist()
    test.test_add_event_name_exist()
    test.test_add_event_data_type_error()
    test.test_add_event_success()