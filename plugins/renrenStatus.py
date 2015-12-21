#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jianwei Fu
#   E-mail  :   jianwei1031@gmail.com
#   Date    :   15/12/21 12:16:30
#   Desc    :   
#

def RenrenStatus():
		username = ''
		password = ''
		# cont = Content.decode('utf-8').encode('utf-8','ignore')
		cont = ''
		neirong = Content.split()
		for i in range(len(neirong)):
			neirong[i] = neirong[i].encode('utf8')
			if i >= 1:
				cont += neirong[i]

		logpage = "http://www.renren.com/ajaxLogin/login"


		datae = {'email': username, 'password': password}
		login_data = urllib.urlencode(datae)
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		urllib2.install_opener(opener)
		res = opener.open(logpage, login_data)
		# rq = urllib2.urlopen(logpage,login_data)
		res2 = urllib2.urlopen("http://www.renren.com/home")

		html1 = res2.read()
		# uid = re.search("'ruid':'(\d+)'", html1).group(1)
		uid_b = html1.find("'ruid':'")
		uid_e = html1.find(",", uid_b)
		uid = html1[uid_b + 8:uid_e - 1]

		req_token_b = html1.find("get_check:'")
		bg = html1.find(",", req_token_b)
		req_token = html1[req_token_b + 11:bg - 1]

		rtk_b = html1.find("get_check_x:'", req_token_b)
		bgg = html1.find(",", rtk_b)
		rtk = html1[rtk_b + 13:bgg - 1]

		links = 'http://shell.renren.com/' + str(uid) + '/status'
		post_data = {
			'content': cont,
			'withInfo': '{"wpath":[]}',
			'hostid': uid,
			'privacyParams': '{"sourceControl": 99}',
			'requestToken': req_token,
			'_rtk': rtk,
			'channel': 'renren'
		}
		login_d = urllib.urlencode(post_data)
		some_test = urllib2.urlopen(links, login_d)  #.read().encode('utf-8','ignore')
		time.sleep(1)
		if len(cont) > 0:  #some_test.find(neirong[1])>0:
			return '已经成功发布了哦!\n<a href="http://3g.renren.com/profile.do?id=562371799">点击链接查看你发布的内容吧</a>'
		else:
			return '出错啦T_T，status后面有空格，还要有需要发布内容哦\n查看help吧'
	#