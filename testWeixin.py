#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import wechatsogou

class WeixinTest:
    url = 'https://mp.weixin.qq.com/profile?src=3&timestamp=1514904552&ver=1&signature=7hBnjJ*dXYUGaM7eh47MxkgXIX9ELZ7Yx4CRKVKmREb8lPeXhKc*S8wKn0qCDhFlXkmYmi2C7DitrMezM3InHw=='
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    def parseUlr(self):
        response = requests.get(self.url,self.headers)
        if(response.status_code == 200):
            print 'fetch ok'
            content = response.content
            print content
            content = content[content.find('{\"list\"'):content.rfind('}}]}')+4]
            print 'handle after:' + content
            try:
                content = json.loads(content)
            except ValueError:
                print 'value error'
        else:
            print 'error'
        
        listItem = content['list']
        for e in listItem:
            print "content item:"+str(e)
            app_msg_info = e['app_msg_ext_info']
            print "url is "+app_msg_info['content_url']

if __name__ == "__main__":
    ws_api =wechatsogou.WechatSogouAPI()
    print ws_api.get_gzh_article_by_history('高可用架构')
    # weixin = WeixinTest()
    # weixin.parseUlr()

