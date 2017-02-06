# -*- coding: utf-8 -*-
import hashlib
import web
import lxml.etree as etree
import time
import os
from imgtest import imgtest
class WeixinInterface:
	
	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root,'templates')
		self.render = web.template.render(self.templates_root)
		
	def GET(self):
		#获取输入参数
		data = web.input()
		signature = data.signature
		timestamp = data.timestamp
		nonce = data.nonce		
		echostr = data.echostr
		#填写自己的Token
		token = u'cs781176645hhh' #这里改写你在微信公众平台里输入的token
		#字典序排序
		list = [token,timestamp,nonce]
		list.sort()
		sha1 = hashlib.sha1()
		map(sha1.update,list)
		hashcode = sha1.hexdigest()
		#sha1加密算法
		
		#如果是来自微信的请求，则回复echostr
		if hashcode == signature:
			return echostr
			
	def POST(self): 
		str_xml = web.data() #获得post来的数据
		xml = etree.fromstring(str_xml)#进行XML解析
		msgType = xml.find("MsgType").text
		fromUser = xml.find("FromUserName").text
		toUser = xml.find("ToUserName").text
		if msgType == 'text':
			content = xml.find("Content").text
			return self.render.reply_text(fromUser,toUser,int(time.time()), content)
		elif msgType == 'image':
			try:
				#拿到系统生成的图片链接
				picurl = xml.find('PicUrl').text
				datas = imgtest(picurl)
				return self.render.reply_text(fromUser, toUser, int(time.time()), r'图中人物性别为'+datas[0]+'\n'+'年龄为'+datas[1])
			except:
				return self.render.reply_text(fromUser, toUser, int(time.time()), r'我只能识别人类，不是人的照片就别拿过来了')
				
		else:
			pass
			