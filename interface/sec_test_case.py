#coding:utf-8
import requests
import os,sys
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import json

class GetEventListTest(object):
    '''查询发布会信息(带用户认证)'''
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_get_event_list/"
    def test_get_event_list_auth_null(self):
        '''auth为空'''
        r=requests.get(self.base_url,params={'eid':1})
        result=r.json()
        print(result)
    def test_get_event_list_auth_error(self):
        '''auth错误'''
        auth_user=('abc','123')
        r = requests.get(self.base_url,auth=auth_user, params={'eid': 1})
        result = r.json()
        print(result)
    def test_get_event_list_eid_null(self):
        '''eid参数为空'''
        auth_user = ('admin', 'admin123456')
        r = requests.get(self.base_url, auth=auth_user, params={'eid':''})
        result = r.json()
        print(result)
    def test_get_event_list_eid_success(self):
        '''根据eid查询结果成功'''
        auth_user = ('admin', 'admin123456')
        r = requests.get(self.base_url, auth=auth_user, params={'eid': '1'})
        result = r.json()
        print(result)

        result=json.dumps(r.json(),indent=2)
        print(type(result))                        #dict
        print(type(json.dumps(result)))            #str   json.dumps():把dict转为str
        print(type(json.loads(json.dumps(result))))#dict  json.loads():把str转为dict
if __name__ == '__main__':
    test=GetEventListTest()
    test.test_get_event_list_auth_null()
    test.test_get_event_list_auth_error()
    test.test_get_event_list_eid_null()
    test.test_get_event_list_eid_success()