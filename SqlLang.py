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

#def CreateData():
#    db=MySQLdb.connect("localhost","root","123456","db_Lang")
#    cursor=db.cursor()
#    sql="""CREATE TABLE HOME (
#        HOMEID INT(4) NOT NULL,
#        TOTAL INT NOT NULL,
#        EXTRAL INT NOT NULL,
#        USERID CHAR(20) NOT NULL,
#        PRIMARY KEY(HOMEID)
#        ) """
#    cursor.execute(sql)
#    db.close()
#def CreateTable():
#    db=MySQLdb.connect("localhost","root","123456","db_Lang")
#    cursor=db.cursor()
#    sql="""CREATE TABLE PLAY (
#        HOMEID INT(4) NOT NULL,
#        PALYNAME CHAR(20) NOT NULL,
#        USERID CHAR(20) NOT NULL,
#        FLAG INT NOT NULL
#        ) """
#    cursor.execute(sql)
#    db.close()
def join(da):
    return da
#def Join(homeid):
#    db=MySQLdb.connect("localhost","root","123456","db_Lang")
#    cursor=db.cursor()
#    sql ="SELECT HOMEID FROM HOME WHERE HOMEID='%d'"%(homeid)
#    cursor.execute(sql)
#    results=cursor.fetchall()
#    if results:
#        sql ="SELECT TOTAL,EXTRAL FROM HOME WHERE HOMEID='%d'"%(homeid)
#        cursor.execute(sql)
#        results=cursor.fetchall()
#        num=results[0][1]
#        total=results[0][0]
#        if num==0:
#            return "房间人数已满"
#        else:
#            n=num-1
#            sql="update HOME set EXTRAL='%d' WHERE HOMEID='%d'"%(n,homeid)
#            cursor.execute(sql)
#            db.commit()
#            while 1:
#                n=random.randint(0,total)
#                sql ="SELECT PALYNAME FROM PLAY WHERE usenum='%d'and HOMEID='%d'and FLAG='1'"%(n,homeid)
#                cursor.execute(sql)
#                results=cursor.fetchall()
#                if results:
#                    sql="update PLAY set FLAG='0' WHERE HOMEID='%d' and usenum='%d'"%(homeid,n)
#                    cursor.execute(sql)
#                    db.commit()
#                    str="房间号 %d"%homeid+'\r\n'+"你的身份 "+TRS(results[0][0])+'\r\n'+'你的号码 %d'%n
#                    db.close()
#                    return str
#
#    else:
#        db.close()
#        return  "房间号不存在，请创建房间"
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
