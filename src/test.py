# -*- coding:utf-8 -*-

# from util import helper
# import time

# headers = {"Json-Rpc-Tonce": time.time() * 1000}
# # params = "{\"jsonrpc\": \"2.0\", \"method\": \"web3_clientVersion\", \"params\": [], \"id\": 1}"
# params = "{\"jsonrpc\": \"2.0\", \"method\": \"eth_getBalance\", \"params\": [\"0x341bedf95e81d45393d4365f03b317a3af3b97dd\", \"latest\"], \"id\": 1}"
#
# response = helper.httpPost("127.0.0.1", 8545, params, headers)
# print(response)

# headers = {"Json-Rpc-Tonce": time.time() * 1000}
# # params = "{\"jsonrpc\": \"2.0\", \"method\": \"web3_clientVersion\", \"params\": [], \"id\": 1}"
# params = "{\"jsonrpc\": \"2.0\", \"method\": \"eth_getBalance\", \"params\": [\"0x341bedf95e81d45393d4365f03b317a3af3b97dd\", \"latest\"], \"id\": 1}"
# ip = "192.168.1.29"
# response = helper.httpPost(ip, 8888, params, headers)
# # print(response)


# import httplib
#
# headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# conn = httplib.HTTPConnection("192.168.1.29", 8888)
# conn.request("GET", "/v1/chain/get_info", "", headers)
# response = conn.getresponse()
# data = response.read()
# print (data)
# conn.close()


import httplib

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = httplib.HTTPConnection("github.com")
conn.request("GET", "/Zzitao/ZeroNet/blob/master/version", "", headers)
response = conn.getresponse()
data = response.read()
print (data)
conn.close()


# balance = httpPost("http://127.0.0.1:8545", {"jsonrpc": "2.0", "method": "eth_coinbase", "params": [], "id": 64})
# print(balance)
#
# import httplib
#
# # 导入需要的python模块urllib，用来对数据进行编码
# import urllib
#
# # 定义请求头
#
# # reqheaders = {'Content-type': 'application/x-www-form-urlencoded',
# #               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #               'Host': 'www.renren.com',
# #               'Origin': 'http://zhichang.renren.com',
# #               'Referer': 'http://zhichang.renren.com',
# #               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1', }
#
# reqheaders = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# # 定义post的参数
#
# # reqdata={'email':'xxxx@xxx.com',
# # 'password':'xxxx',
# # 'autoLogin':'on',
# # 'origURL':'http://zhichang.renren.com/?login_state=rr',
# # 'domain':'renren.com'
# # }
# reqdata = {"jsonrpc": "2.0", "method": "eth_coinbase", "params": [], "id": 64}
#
# # 对请求参数进行编码
#
# data = urllib.urlencode(reqdata)
#
# # 利用httplib库模拟接口请求
#
# # 先连接到人人
#
# conn = httplib.HTTPConnection('127.0.0.1', 8545)
#
# # 提交登录的post请求
# conn.request('POST', '', data, reqheaders)
#
# # 获取服务器的返回
# res = conn.getresponse()
#
# # 打印服务器返回的状态
# # print(res.status)
#
# # 以dictionary形式答应服务器返回的 response header
#
# print(res.msg)
# # 打印服务器返回请求头中设置的cookie
# # print(res.getheader('Set-Cookie'))
# print(res.read())
