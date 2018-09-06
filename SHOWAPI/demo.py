# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/12 17:14'

from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/630-1",64754,"F287040DCE8D88EA7487217AD30DB5E4" )
# r.addFilePara("img", r"C:\Users\showa\Desktop\使用过的\4.png") #文件上传时设置
res = r.post()
print(res.text) # 返回信息