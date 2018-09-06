#coding:utf-8
import requests
import unittest

class GetEventListTest(object):
    '''查询发布会接口测试'''
    # def setUp(self):
    #     self.url="http://127.0.0.1:8000/api/get_event_list/"
    def __init__(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"
    def test_get_event_null(self):
        '''发布会id为空'''
        # print '---------'
        r=requests.get(self.url,params={'eid':''})
        result=r.json()
        print(result)
        # print(result['status'])
        # print(result['message'])
    def test_get_event_error(self):
        '''发布会id不存在'''
        r=requests.get(self.url,params={'eid':'901'})
        result=r.json()
        print(result)
        # print(result['status'])
        # print(result['message'])

    def test_get_event_success(self):
        '''发布会id为1，查询成功'''
        r=requests.get(self.url,params={'eid':'1'})
        result=r.json()
        print(result)
        # print(result['status'])
        # print(result['message'])
        # print(result['data']['name'])
        # print(result['data']['address'])
        # print(result['data']['start_time'])

if __name__ == '__main__':
    test=GetEventListTest()
    test.test_get_event_null()
    test.test_get_event_error()
    test.test_get_event_success()


