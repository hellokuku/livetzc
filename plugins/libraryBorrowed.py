#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jianwei Fu
#   E-mail  :   jianwei1031@gmail.com
#   Date    :   15/12/21 12:16:38
#   Desc    :   
#
import urllib,urllib2,cookielib


def LibraryBorrowed(username,password):
		try:
			logpage = 'http://www2.lib.tzc.edu.cn/cgi-bin/confirmuser'
			books_all = []
			data1 = {
				'v_newuser': '0',
				'v_regname': '',
				'v_cardno': username,
				'v_passwd': password
			}
			login_data = urllib.urlencode(data1)
			cj = cookielib.CookieJar()
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			urllib2.install_opener(opener)
			res = opener.open(logpage, login_data)
			html = res.read().decode('gb2312').encode('utf-8')
			if html.find('javascript:ModifyPasswd()') > 0:
				books = urllib2.urlopen('http://www2.lib.tzc.edu.cn/cgi-bin/SrchLoan').read().decode('gb2312','ignore').encode(
					'utf-8')
				if books.find(username) > 0:
					book_nums_s = books.find('普通外借数')
					book_s = books.find('height=', book_nums_s)
					book_nums_b = books.find('>', book_s)
					books_nums_e = books.find('<', book_nums_b)
					borrowed = '恭喜！查询成功!\n您总共借了' + books[book_nums_b + 1:books_nums_e] + '本书\n'
					books_all.append(borrowed)
					while True:
						shu = books.find('td colspan="3" bgcolor="white" width="50%')
						if shu > 0:
							shu_b = books.find('>', shu)
							shu_e = books.find('<', shu_b)
							jiedeshu = '<<' + books[shu_b + 1:shu_e] + '>>'
							books_all.append(jiedeshu)
							guihuan = books.find('应还日期')
							guihuan2 = books.find('<td bgcolor="white" width="*"', guihuan)
							guihuan_begin = books.find('>', guihuan2)
							guihuan_end = books.find('<', guihuan_begin)
							guihuanriqi = books[guihuan_begin + 1:guihuan_end]
							books_all.append('\n应还日期:')
							books_all.append(guihuanriqi)
							books_all.append('\n')
							books = books[guihuan_end:]
						else:
							break
					Content = ''
					for x in books_all:
						Content += x
					if len(Content) == 0:
						return '您没有已借的书籍!要多努力看书哦!'
					else :
						return Content
				else:
					return '【密码错误哦!】\n现已经转为一卡通.用户名为学号,密码为原图书证帐号密码,如果忘记了可以到图书馆一楼大厅重置密码呢!1'

			else:
				return '【密码错误哦!】\n现已经转为一卡通.用户名为学号,密码为原图书证帐号密码,如果忘记了可以到图书馆一楼大厅重置密码呢!2'
		except:
			return 'sorry...borrowed..'

if __name__ == '__main__':
	pass