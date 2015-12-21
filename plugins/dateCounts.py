#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jianwei Fu
#   E-mail  :   jianwei1031@gmail.com
#   Date    :   15/12/21 12:16:19
#   Desc    :   
#

from datetime import date

def DateCounts(Content):
		test = Content.split()
		if len(test) == 2:
			d = test[1]
			if len(d) == 8:
				year = int(d[0:4])
				month = int(d[4:6])
				day = int(d[6:])
				bir = date(year, month, day)
				now = date.today()
				age = now - bir
				return '你一共活了%d天啦!要多珍惜时间呀!' % age.days
			else:
				return '要输入正确的格式哦^_^1'
		else:
			return '要输入正确的格式哦^_^2'