#coding:utf-8
import requests,hashlib
from time import time
from db_fixture import test_data

class AddEventTestMd5(object):
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_add_event/"
        self.api_key="&Guest-Bugmaster"
        now_time=time()
        self.client_time=str(now_time).split('.')[0]
        md5=hashlib.md5()
        sign_str=self.client_time+self.api_key
        sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
        md5.update(sign_bytes_utf8)
        self.sign_md5=md5.hexdigest()
    def test_add_event_request_error(self):
        '''请求方法错误'''
        r=requests.get(self.base_url)
        result=r.json()
        print(result)
    def test_add_event_sign_null(self):
        '''签名参数为空'''
        payload={'eid':1,'':'','limit':'','address':'','start_time':'','time':'','sign':''}
        r=requests.post(self.base_url,data=payload)
        result=r.json()
        print(result)
    def test_add_event_time_out(self):
        '''请求超时'''
        now_time=str(int(self.client_time)-61)
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '', 'time': now_time, 'sign': 'abc'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
    def test_add_event_sign_error(self):
        '''签名错误'''
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '', 'time': self.client_time, 'sign': 'abc'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
    def test_add_event_success(self):
        '''添加成功'''
        payload = {'eid': 21, 'name': '一加5手机发布会', 'limit': '2000','address': '深圳宝体',
                   'start_time': '2019-08-20 00:25:42', 'time': self.client_time,'sign':self.sign_md5}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        print(result)
if __name__ == '__main__':
    test_data.init_data()
    test=AddEventTestMd5()
    test.test_add_event_request_error()
    test.test_add_event_sign_null()
    test.test_add_event_time_out()
    test.test_add_event_sign_error()
    test.test_add_event_success()