# LangGame
利用python设计一个狼人杀游戏

我们先要了解，狼人杀游戏的发牌逻辑，

逻辑：
  
  1.每个人放一张牌，而且每个人的身份固定，也就是说，你的牌对应你是几号，当我们发完这张 牌的时间，后面的人就不能再发这张牌了
  
  2.还有房间号，我们在玩一个游戏的时间要加入游戏即就是加入房间号和创建房间号
  
  3.我们加入房间后我们就在这个房间里玩游戏，
  
实现方法：

  1.我们先创建房间，我们在数据库，专门开创一个房间表。
  
  2.我们加入房间时，我们在数据库里查找是否有相对应的房间号。
  
  3.没有的话，返回“请创建房间”，有的话，将我们的用户更新到房间表里
  
  4.开始游戏后，我们分牌，我们将我们的id和牌一一对应
  
  5.分完，我们将标志位修改成1，没分我们将牌的标志位默认为0
  
  6.当牌的标志位全为1时，我们就将牌分完了
  
  7.我们将游戏表里的数据一一反馈给用户
  
  具体的数据表的设计，博客：http://blog.csdn.net/xuaomo/article/details/75195726
  ![image](http://img.blog.csdn.net/20170716092708749?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveHVhb21v/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
  ![image](http://img.blog.csdn.net/20170716092724984?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveHVhb21v/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
  ![image](http://img.blog.csdn.net/20170716092735316?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveHVhb21v/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
  ![iamge](http://img.blog.csdn.net/20170716093203979?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveHVhb21v/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
