#!/usr/bin/env python
# coding=utf-8
import MySQLdb
import random
def TRS(name):
    if name =='Hunter':
        return '猎手'
    elif name=='Wolf':
        return '狼人'
    elif name=='Prophet':
        return '预言家'
    elif name=='Witch':
        return '女巫'
    elif name =='Civilians':
        return '平民'
#def CreateTableLANG_PLAYER():#调用直接生成LANG_PLAYER表格
#    db=MySQLdb.connect("localhost","root","123456","db_Lang")
#    cursor=db.cursor()
#    sql="""CREATE TABLE LANG_PLAY (
#        NUM INT(4) NOT NULL,
#        CONUT CHAR(20) NOT NULL,
#        EXTRAL CHAR(20) NOT NULL,
#        USERID INT NOT NULL,
#        ) """
#    cursor.execute(sql)
#    db.close()

#def CreateTablePALY():#调用直接生成PALY表格
#    db=MySQLdb.connect("localhost","root","123456","db_Lang")
#    cursor=db.cursor()
#    sql="""CREATE TABLE PLAY (
#        HOMEID INT(4) NOT NULL,
#        PALYNAME CHAR(20) NOT NULL,
#        USERID CHAR(20) NOT NULL,
#        FLAG INT NOT NULL,
#        usernum INT(4) NOT NULL
#        ) """
#    cursor.execute(sql)
#    db.close()
def Inser(userid,num):
    db=MySQLdb.connect("localhost","root","123456","db_Lang")
    cursor=db.cursor()
    homeid=random.randint(1000,9999)
    sql="INSERT INTO HOME(HOMEID,TOTAL,EXTRAL,USERID) VALUES('%d', '%d','%d','%s')"%(homeid, num,num,userid)
    str="房间 %d\r\n"%homeid
    cursor.execute(sql)
    db.commit()
    list=range(1,num+1)
    random.shuffle(list)
    for k in range(0,num):
        n=list[k]
        if k <3:
            pla=['Hunter','Witch','Prophet']
            platername=pla[k]
            str=str+"%d号 %s \r\n"%(n,TRS(platername))
            sql="INSERT INTO PLAY(HOMEID,PALYNAME,USERID,FLAG,usenum) VALUES('%d', '%s','%s',1,'%d')"%(homeid, platername,userid,n)
            cursor.execute(sql)
            db.commit()
        else:
            pla=['Civilians','Wolf']
            i=k%2
            if i==1:
                platername=pla[1]
            else :
                platername=pla[0]
            str=str+"%d号 %s \r\n"%(n,TRS(platername))
            sql="INSERT INTO PLAY(HOMEID,PALYNAME,USERID,FLAG,usenum) VALUES('%d', '%s','%s',1,'%d')"%(homeid, platername,userid,n)
            cursor.execute(sql)
            db.commit()

    db.close()
    return str
