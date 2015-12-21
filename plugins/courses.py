#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jianwei Fu
#   E-mail  :   jianwei1031@gmail.com
#   Date    :   15/12/21 12:16:48
#   Desc    :   
#
import sae.storage
def Courses(Content):
		kebiao = Content.split()
		try:
			numxh = int(kebiao[0])
			shijian = str(kebiao[1])
			s = sae.storage.Client()
			s.list_domain()
			ob = s.get('201403kebiao', str(numxh) + '.txt')
			ob = ob.data
			hello1 = ob.splitlines()
			Content = ''
			for shi in hello1:
				if shijian == '1' and '周一' in shi:
					Content += shi
					Content += '\n++++++++++++\n'
				elif shijian == '2' and '周二' in shi:
					Content += shi
					Content += '\n++++++++++++\n'
				elif shijian == '3' and '周三' in shi:
					Content += shi
					Content += '\n++++++++++++\n'
				elif shijian == '4' and '周四' in shi:
					Content += shi
					Content += '\n++++++++++++\n'
				elif shijian == '5' and '周五' in shi:
					Content += shi
					Content += '\n++++++++++++\n'
			if len(Content) == 0:
				return '好羡慕T_T!!!!!!\n你!今!天!居!然!没!课!'
		except:
			return '非常抱歉!您的数据没有录入或者学号不存在!\n\n欢迎加开发者帐号QQ:563125575^_^\nAnyway,谢谢支持!\n输入help查看具体功能'
