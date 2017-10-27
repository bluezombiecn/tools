#!/usr/bin/python
#coding=utf-8
import json
import urllib2

url = "https://oapi.dingtalk.com/robot/send?access_token=50a8c22477f2b50c3c67343cfbd50dfcdd87308d83d3a28797f5ecac08afbe86"
header = {
    "Content-Type":"application/json",
    "Charset":"utf-8"
}
data = {
    "msgtype":"text",
    "text":{
        "content":"Hello Opsers!"
    },
    "at":{
        "isAtAll":True
    }
}

# markdown
'''
data = {
    "msgtype":"markdown",
    "markdown":{
        "title":"Title",
        "text":"# 标题1\n"+
                "> ```test markdown```\n"+
                "> ![jpg](http://wx2.sinaimg.cn/bmiddle/e1ceda65gy1fj1i3x8e3uj20mi0xc79y.jpg)"
    },
    "at":{
        "isAtAll":True
    }
}
'''
sendData = json.dumps(data)
requestData = urllib2.Request(url,data = sendData,headers = header)
opener = urllib2.urlopen(requestData)
print opener.read()
