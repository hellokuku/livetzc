#! /usr/bin/env python
# -*- coding:utf8 -*-
import time
from flask import Flask, g, request, make_response
import hashlib, urllib2, urllib, re, cookielib
import xml.etree.ElementTree as ET
import sae.storage
from datetime import date
import requests
import json
import config
import dateCounts,lrcSearch,renrenStatus,bus,movies, schoolCalendar,courses,music
import libraryBorrowed,librarySearch

tips = config.tips
error_msg = config.error_msg

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def wechat_auth():
	if request.method == 'GET':
		token = 'Add your token here'
		query = request.args
		signature = query.get('signature', '')
		timestamp = query.get('timestamp', '')
		nonce = query.get('nonce', '')
		echostr = query.get('echostr', '')
		s = [timestamp, nonce, token]
		s.sort()
		s = ''.join(s)
		if ( hashlib.sha1(s).hexdigest() == signature ):
			return make_response(echostr)
	# Get the infomations from the recv_xml.
	reply = config.reply
	xiaoli_reply = config.xiaoli_reply
	bus_reply = ''' '''
	xml_recv = ET.fromstring(request.data)
	ToUserName = xml_recv.find("ToUserName").text
	FromUserName = xml_recv.find("FromUserName").text
	Content = ''
	try:
		Content = xml_recv.find("Content").text
	except:
		pass
	msgtype_test = ''
	event_test = ''
	try:
		msgtype_test = xml_recv.find('MsgType').text
		event_test = xml_recv.find('Event').text
	except:
		pass

	if msgtype_test == 'event' and event_test == 'subscribe':
		# 返回帮助信息
		Content = tips

	elif Content.lower().find('xiaoli') >= 0:
		# 返回图文模式
		# 校历
		response = make_response(xiaoli_reply % (
			FromUserName, ToUserName, str(int(time.time())), 'http://tzclife-pic.stor.sinaapp.com/xiaoli2015.jpg' ))
		response.content_type = 'application/xml'
		return response

	elif Content.lower().find('help') >= 0:
		# 返回帮助信息
		Content = tips

	elif Content.lower().find('bir') >= 0:
		# 返回天数
		Content = dateCounts.DateCounts(Content)

	elif Content.lower().find('time') >= 0 :
		# 查询校园时间表
		Content = config.TimeTableSummer

	elif Content.lower().find('movie') >= 0 :
		# 查询学校电影信息
		Content = config.movies

	elif Content.lower().find('bus') >= 0 :
		# 查询公交信息
		Content = config.bus

	elif Content.lower().find('status') >= 0 :
		# 向人人网LiveTzc发布状态
		Content = renrenStatus.RenrenStatus(Content)

	elif Content.find('@') >= 0:
		# 查询歌词 用的是百度音乐
		Content = lrcSearch.LrcSearchRequests(Content)

	elif Content.find('dt') >= 0:
		# 查询上海公交卡还剩多少钱
		sptccUrl = 'http://220.248.75.36/handapp/PGcardAmtServlet?arg1='
		success = Content.split()
		if len(success) == 2:
			page = urllib2.urlopen(sptccUrl + success[1]).read()
			page_f = page.find("'")
			page_e = page.find("'", page_f + 1)
			Content = '交通卡还剩下  ' + page[page_f + 1:page_e] + '  元TAT'
		else:
			Content = 'SPTCC error...'

	elif Content.find('car') >= 0:
		# 查询违章信息
		args = Content.split()
		chepai = args[1]
		cjh = args[2]
		post_url = 'http://bsdt.jhga.gov.cn/egov/jdcwfcxAction.action'
		post_data = dict(CPHM='浙G' + chepai, CJH=cjh, CPLB='02', fn='jdcwfcx', OPENID='oDQPZt6mijPGQMBv7cnAOOUBK8g8')
		html = requests.post(post_url, post_data)
		try:
			datas = json.loads(html.content)
			carid = len(datas)
			infos = ''
			for x in range(carid):
				infos = infos + '\n\nwww.jhga.gov.cn/ajax/jxj_showimg.aspx?id='+str(datas[x]['ID'])
			Content = html.content[:1500]+'\n'+'一共'+str(carid)+'个违章\n\n'+ infos[:460]
		except:
			Content = html.content[:2000]

	elif Content.lower().find('cjhlist') >= 0:
		# 违章列表
		Content =  config.cars

	elif Content.lower().find('sptcc') >= 0:
		# 查询上海公交卡还剩多少钱
		sptccUrl = 'http://220.248.75.36/handapp/PGcardAmtServlet?arg1=49925366539'
		page = urllib2.urlopen(sptccUrl).read()
		page_f = page.find("'")
		page_e = page.find("'", page_f + 1)
		Content = '交通卡还剩下  ' + page[page_f + 1:page_e] + '  元TAT'

	elif Content.lower().find('lib') >= 0 :
		# 图书馆相关信息查询
		success = Content.split()
		book_url = 'http://www2.lib.tzc.edu.cn/cgi-bin/IlaswebBib'
		for i in range(len(success)):
			success[i] = success[i].encode('utf8')
		if len(success) == 2:
			book_name = success[1]
			Content = librarySearch.LibrarySearch(book_name)

		elif len(success) == 3:
			try:
				Content = libraryBorrowed(success[1],success[2])
			except:
				Content = '图书馆服务器故障'
		else:
			Content = 'lib和书名之间要有个空格哦!!!'

	elif len(Content.split()) == 2:
		# 返回课表信息
		Content = courses.Courses(Content)
	else:
		Content = error_msg
	# 格式化
	response = make_response(reply % (FromUserName, ToUserName, str(int(time.time())), Content ))
	response.content_type = 'application/xml'
	return response


