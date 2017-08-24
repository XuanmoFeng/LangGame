# -*- coding: utf-8 -*-
import hashlib
import web
import auoth
import reply
import receive
class Handle(object):
    def POST(self):
        try:
            webData=web.data()
            recMsg =receive.parse_xml(webData)
            if isinstance(recMsg,receive.Msg):
                toUser=recMsg.FromUserName
                fromUser=recMsg.ToUserName
                if recMsg.MsgType =='text':
                    content=auoth.Text(toUser,recMsg.Content)#自动回复接口
                    replyMsg=reply.TextMsg(toUser,fromUser,content)
                    return replyMsg.send()
                if recMsg.MsgType=='image':
                    mediaId=recMsg.MediaId
                    replyMsg=reply.ImageMsg(toUser,fromUser,mediaId)
                    return replyMsg.send()
            #if isinstance(recMsg,receive.EventMsg):        #菜单
            #    if recMsg.Event=='CLICK':
            #        if recMsg.Eventkey =='mpGuide':
            #            content=u"编写中，尚未完成"
            #            reply=reply.TextMsg(toUser,fromUser,content)
            #            return reply.send()
            else:
                print "暂不处理"
                return reply.Msg().send()
        except Exception,Argument:
            return Argument
    def GET(self):
         try:
             data = web.input()
             if len(data) == 0:
                 return "hello, this is handle view"
             signature = data.signature
             timestamp = data.timestamp
             nonce = data.nonce
             echostr = data.echostr
             token = "weixin" #请按照公众平台官网\基本配置中信息填    
             list = [token, timestamp, nonce]
             list.sort()                        
             sha1 = hashlib.sha1()
             map(sha1.update, list)
             hashcode = sha1.hexdigest()
             print "handle/GET func: hashcode, signature: ", hashcode, signature
             if hashcode == signature:
                 return echostr
             else:
                 return ""
         except Exception, Argument:
             return Argument
