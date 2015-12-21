#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jianwei Fu
#   E-mail  :   jianwei1031@gmail.com
#   Date    :   15/12/21 12:05:03
#   Desc    :   
#
import urllib,urllib2,re


def LibrarySearch(bookname):
		try:
			book_url = 'http://www2.lib.tzc.edu.cn/cgi-bin/IlaswebBib'
			book_name = bookname
			shumu = {
				'v_index': 'TITLE',
				'v_value': book_name.decode('utf-8').encode('gb2312', 'ignore'),
				'FLD_DAT_BEG': '',
				'FLD_DAT_END': '',
				'v_pagenum': '20',
				'v_seldatabase': '0',
				'v_LogicSrch': '0',
				'submit': '查 询'.decode('utf-8').encode('gb2312', 'ignore')
			}
			login_data = urllib.urlencode(shumu)
			html = urllib2.urlopen(book_url, login_data).read().decode('gb2312', 'ignore').encode('utf-8')
			Content = ''
			try:
				p = re.findall('<td align=left height=25 bgcolor=\"#FFFFFF\">(.*)<', html)
				timej = 0
				leap = 0
				Content = ''
				for x in p:
					timej += 1
					if timej % 6 == 1:
						Content += '【'
						Content += x
						Content += '】'
						Content += '\n'
					elif timej % 6 == 0:
						Content += '书架号:'
						Content += x
						Content += '\n'
				if len(Content) == 0:
					return '该书图书馆还未收录!你可以尝试建议图书馆管理员进这本书哦!'
				else:
					return Content
			except:
				return  '抱歉图书馆服务器暂时无法连接,请稍后再试!'
		except:
			return 'sorry'

if __name__ == '__main__':
	content = LibrarySearch('python')
	print content