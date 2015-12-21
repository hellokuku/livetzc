#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jianwei Fu
#   E-mail  :   jianwei1031@gmail.com
#   Date    :   15/12/20 21:42:26
#   Desc    :   
#

tips = '''
o(≧o≦)o
欢迎主人使用LiveTzc!
现在已具有的功能有:
①【课表查询】
回复 学号数字 周几数字
如"1234219999 5"
(注意空格)就可查该同学周五课表
②【时间表查询】
回复 time
③【校历查询】
回复 xiaoli
④【图书馆书目查询】
如回复 lib 微积分
⑤【已借书籍归还日期查询】
回复 lib 学号 图书证密码
⑥【台院影剧院电影查询】
回复 movie
⑦【公交车查询】
回复 bus 台州学院
同时支持2个地名哦
注意空格默认最多返回2个结果
⑧【歌词查询】
回复 歌名@歌手)
如 但愿人长久@王菲
⑨【成长几天】
    回复 birthday 出生日期
    如 birthday 19990101
⑩【状态发布】
回复 status 想要说的话
＝【微社区】
回复 shequ
'''

error_msg = '''
o(≧o≦)o!
出错咯!输入指令不符合要求呢!
快输入help求救我吧!

LiveTzc微社区地址：http://wx.wsq.qq.com/236373815


联系开发者QQ563125575'''

reply = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
<FuncFlag>0</FuncFlag>
</xml>'''

xiaoli_reply = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<Content><![CDATA[]]></Content>
<ArticleCount>1</ArticleCount>
<Articles>
<item>
<Title><![CDATA[台州学院2015-2016校历\nTaizhou University]]></Title>
<Description><![CDATA[澡身浴德、修业及时]]></Description>
<PicUrl><![CDATA[%s]]></PicUrl>
<Url><![CDATA[http://tzclife-pic.stor.sinaapp.com/xiaoli2015.jpg]]></Url>
</item>
</Articles>
<FuncFlag>0</FuncFlag>
</xml>'''

TimeTableSummer = '''
五月一日起采用夏令作息时间表

    『夏令作息时间表』
    第一节:    08：00～08：40
    第二节:    08：50～09：30
    第三节:    09：40～10：20
    第四节:    10：30～11：10
    第五节:    11：20～12：00
    第六节:    14：00～14：40
    第七节:    14：50～15：30
    第八节:    15：40～16：20
    第九节:    16：30～17：10
    第十节:    19：00～19：40
    第十一节:19：50～20：30
    第十二节:20：40～21：20'''

TimeTableWinter = '''

'''

movies = '''
主人要注意劳逸结合哦/可爱!
9.01-9.02 <天台>
9.03-9.04 <小时代>
9.05-9.06 <不二神探>
9.07-9.08 <金太郎的幸福生活>
9.11-9.12 <光辉岁月>
9.13-9.14 <太极侠>
9.22-9.23 <速度与激情6>
9.24-9.25 <惊天危机>
9.26-9.27 <钢铁侠>
单场票价3元
电影播放时间分别为:
18:30/20:10
'''

bus = '''
BUS终于来啦
<a href="http://m.8684.cn/linhai_bus">临海BUS</a>\n
<a href="http://m.8684.cn/taizhou2_bus">椒江BUS</a>\n
<a href="http://m.8684.cn/yiwu_bus">义乌BUS</a>
主页菌是义乌侬，欢迎老乡加好友！^_^\n
<a href="http://m.8684.cn/">其他地区BUS</a>
'''

cars = '''
'''
