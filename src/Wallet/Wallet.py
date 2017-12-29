# -*- coding:utf-8 -*-
class Wallet(object):
    def __getattr__(self, func_name):
        return getattr(self, func_name)

    def actoinGetNewAddress(self):
        print("actoinGetNewAddress")
        pass

    def actoinGetBalance(self, address, type='latest', coinType='ETH'):
        print ("actoinGetBalance")
        from util import helper
        response = None
        if coinType == 'ETH':
            import time
            address = "0x341bedf95e81d45393d4365f03b317a3af3b97dd"
            headers = {"Json-Rpc-Tonce": time.time() * 1000}
            params = "{\"jsonrpc\": \"2.0\", \"method\": \"eth_getBalance\", \"params\": [\"" + address + "\", \"" + type + "\"], \"id\": 1}"

            response = helper.httpPost("127.0.0.1", 8545, params, headers)
        elif coinType == 'EOS':
            import httplib

            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
            conn = httplib.HTTPConnection("192.168.1.29", 8888)
            conn.request("GET", "/v1/chain/get_info", "", headers)
            response = conn.getresponse()
            data = response.read()
            print (data)
            conn.close()
        print(response)
        pass

    def actoinSendTransactoin(self):
        print("actoinSendTransactoin")
        pass

    def actoinSign(self):
        print ("wallet actoinSign")
        pass


wallet = Wallet()
