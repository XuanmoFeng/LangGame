#!/usr/bin/env python
# coding=utf-8
import urllib2
import json
def getHtml(url):
    page=urllib2.urlopen(url)
    html=page.read()
    return html
def Robot(str):
    key='6994be32f17d5230094834590c0ad8f0'
    url='http://www.tuling123.com/openapi/api?key='+key+'&info='+str
    request=getHtml(url)
    dic_json=json.loads(request,encoding='utf-8')
    return dic_json['text']
