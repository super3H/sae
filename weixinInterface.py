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
				return self.render.reply_text(fromUser, toUser, int(time.time()), ('图中人物性别为:'+datas[0]+'\n'+'年龄为:'+datas[1]).decode('gbk'))
			except:
				return self.render.reply_text(fromUser, toUser, int(time.time()), ('我只能识别人类，不是人的照片就别拿过来了').decode('gbk'))
		elif msgType == 'event':
			mscontent = xml.find("Event").text
			if mscontent == "subscribe":
				replayText = '欢迎关注本微信，这个微信是本人业余爱好所建立，也是想一边学习Python一边玩的东西,现在还没有什么功能，只有人脸识别功能，以后还会继续努力的'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
			if mscontent == "unsubscribe":
				replayText = '我现在功能还很简单，知道满足不了您的需求，但是我会慢慢改进，欢迎您以后再来'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
		else:
			pass
			