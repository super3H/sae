# -*- coding: utf-8 -*-
import hashlib
import web
import lxml.etree as etree
import time
import os
import random
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
			if content.lower().strip() == 'help':
				replayText = '2.输入 book 要查询的书名 返回豆瓣图书中结果\n3.输入cls清除查询记录\n4.输入m随机来首音乐听，建议在wifi下听\n5.输入python 进入python常用模块用法查询（未完成）'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
			if content.lower().strip() == 'm':
				musicList = [[r'http://bjbgp02.baidupcs.com/file/a42866893b395b638b390b2999a82aba?bkt=p3-0000e2dc4d511afc65aa8573cd780a3bb95b&fid=2351452762-250528-756392114883298&time=1486379415&sign=FDTAXGERLBH-DCb740ccc5511e5e8fedcff06b081203-PRskEwRqkH98GLtNAnlKBOMuTA4%3D&to=fbjbgp&fm=Yan,B,G,bs&sta_dx=12315199&sta_cs=8&sta_ft=mp3&sta_ct=0&sta_mt=0&fm2=Yangquan,B,G,bs&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=0000e2dc4d511afc65aa8573cd780a3bb95b&sl=69926991&expires=8h&rt=pr&r=577196619&mlogid=853467811183288326&vuk=2351452762&vbdid=248539820&fin=%E8%B5%B5%E9%9B%B7-%E6%88%90%E9%83%BD.mp3&fn=%E8%B5%B5%E9%9B%B7-%E6%88%90%E9%83%BD.mp3&slt=pm&uta=0&rtype=1&iv=0&isw=0&dp-logid=853467811183288326&dp-callid=0.1.1&csl=500&csign=pzWv8WM4tfK0JUsT5ema4tnAsgg%3D','成都','一首关于成都的民谣']]
				music = random.choice(musicList)
				musicurl = music[0]
				musictitle = music[1]
				musicdes = music[2]
				return self.render.reply_music(fromUser,toUser,int(time.time()),musictitle,musicdes,musicurl)
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
			