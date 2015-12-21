#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jianwei Fu
#   E-mail  :   jianwei1031@gmail.com
#   Date    :   15/12/21 12:16:27
#   Desc    :   
#
import urllib,urllib2
import requests,re

def LrcSearch(song):
		args = song.split('@')
		for i in range(len(args)):
			args[i] = args[i].encode('utf8','ignore')  # pass test
		lrc_link = 'http://music.baidu.com/search/lrc?'
		s = args[0]
		h = {'key': s}
		dse = urllib.urlencode(h)
		linkss = lrc_link + dse
		htmls = urllib2.urlopen(linkss).read()
		begin = htmls.find("/data2/lrc/")
		if begin > 0:
			end = htmls.find("'", begin)
			linkss = 'http://music.baidu.com' + htmls[begin:end]
			return  urllib2.urlopen(linkss).read()[:2000]
		else:
			return  '歌手或者歌名对于有错误哦!\n再仔细想想?\n输入help查看具体功能 test'

def LrcSearchRequests(song):
	args = song.split('@')
	lrcUrl = 'http://music.baidu.com/search/lrc?key='+args[0]
	pageContent = requests.get(lrcUrl).content
	lrcLink = 'http://music.baidu.com' + re.search("<a class=\"down-lrc-btn { 'href':'([^']+)'",pageContent).groups(1)[0]
	lrcContent = requests.get(lrcLink).content
	return lrcContent[:2000]


if __name__ == '__main__':
	content = LrcSearchRequests('七里香@周杰伦')
	print content