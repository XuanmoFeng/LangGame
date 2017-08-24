# -*- coding: utf-8 -*-
# filename: basic.py
import urllib
import time
import json

class Basic:
    def __init__(self):
        self.__accessToken =''
        self.__leftTime = 0
    def __real_get_access_token(self):
       # appId = "wx713b53082b6fe2b2
       # appSecret = "b9301b3396fdb7665245c0b8198b8c34"

        appId="wxc539e8f51feb2fd7"
        appSecret="71bcda94a96bfa65054a99c04b1938b7"
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=""client_credential&appid=%s&secret=%s" % (appId, appSecret))
        urlResp = urllib.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())
        
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']

    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
        return self.__accessToken

    def run(self):
        while(True):
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()
