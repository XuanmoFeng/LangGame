#!/usr/bin/env python
# coding=utf-8
import Rot
import SqlLang
from  string  import maketrans
import www
import Fanyi
import string
import Join
def Text(toUser,UserText):
    content=""
    if UserText=="成绩":
        content=www.Grade(toUser)
    elif UserText.isdigit()&(len(UserText)==4):
        Us=string.atoi(UserText)
        content=Join.Join(Us)
    elif UserText.count('&')==1:#绑定
        ind ="&"
        optd ="@"
        trantab = maketrans(ind,optd)  
        UserText=UserText.translate(trantab)
        content=www.Bind(toUser,UserText)
    elif UserText=="家":
        content="<a href=\"http://119.29.115.52:8080/\">家</a>"
    elif UserText=="公交":
        pass
    elif UserText[0]=="F":
        content=Fanyi.Trans(UserText[1:])
    elif UserText=="豆瓣":
        pass
    elif UserText=="狼人杀":
        content='<a href="https://baike.baidu.com/item/%E7%8B%BC%E4%BA%BA%E6%9D%80/8035581?fr=aladdin#2">新手教程</a>\n回复：狼人杀+X(X表示玩家人数)\n如:狼人杀+8  即8个玩家'
        pass
    elif "狼人杀+"in UserText:
        si=string.atoi(UserText.partition("+")[2])
        if si>=6 & si <=15:
            content=SqlLang.Inser("da",si)+"对我输入房间号来认领身份" 
        else:
            print "人数必须大于5个，小于16,请重新创建房间"
    #else UserText[0:3]
    else:
        content=Rot.Robot(UserText)
    return content
