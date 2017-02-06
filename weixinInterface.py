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
		#��ȡ�������
		data = web.input()
		signature = data.signature
		timestamp = data.timestamp
		nonce = data.nonce		
		echostr = data.echostr
		#��д�Լ���Token
		token = u'cs781176645hhh' #�����д����΢�Ź���ƽ̨�������token
		#�ֵ�������
		list = [token,timestamp,nonce]
		list.sort()
		sha1 = hashlib.sha1()
		map(sha1.update,list)
		hashcode = sha1.hexdigest()
		#sha1�����㷨
		
		#���������΢�ŵ�������ظ�echostr
		if hashcode == signature:
			return echostr
			
	def POST(self): 
		str_xml = web.data() #���post��������
		xml = etree.fromstring(str_xml)#����XML����
		msgType = xml.find("MsgType").text
		fromUser = xml.find("FromUserName").text
		toUser = xml.find("ToUserName").text
		if msgType == 'text':
			content = xml.find("Content").text
			if content.lower().strip() == 'help':
				replayText = '2.���� book Ҫ��ѯ������ ���ض���ͼ���н��\n3.����cls�����ѯ��¼\n4.����m���������������������wifi����\n5.����python ����python����ģ���÷���ѯ��δ��ɣ�'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
			if content.lower().strip() == 'm':
				musicList = [[r'http://bjbgp02.baidupcs.com/file/a42866893b395b638b390b2999a82aba?bkt=p3-0000e2dc4d511afc65aa8573cd780a3bb95b&fid=2351452762-250528-756392114883298&time=1486379415&sign=FDTAXGERLBH-DCb740ccc5511e5e8fedcff06b081203-PRskEwRqkH98GLtNAnlKBOMuTA4%3D&to=fbjbgp&fm=Yan,B,G,bs&sta_dx=12315199&sta_cs=8&sta_ft=mp3&sta_ct=0&sta_mt=0&fm2=Yangquan,B,G,bs&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=0000e2dc4d511afc65aa8573cd780a3bb95b&sl=69926991&expires=8h&rt=pr&r=577196619&mlogid=853467811183288326&vuk=2351452762&vbdid=248539820&fin=%E8%B5%B5%E9%9B%B7-%E6%88%90%E9%83%BD.mp3&fn=%E8%B5%B5%E9%9B%B7-%E6%88%90%E9%83%BD.mp3&slt=pm&uta=0&rtype=1&iv=0&isw=0&dp-logid=853467811183288326&dp-callid=0.1.1&csl=500&csign=pzWv8WM4tfK0JUsT5ema4tnAsgg%3D','�ɶ�','һ�׹��ڳɶ�����ҥ']]
				music = random.choice(musicList)
				musicurl = music[0]
				musictitle = music[1]
				musicdes = music[2]
				return self.render.reply_music(fromUser,toUser,int(time.time()),musictitle,musicdes,musicurl)
			return self.render.reply_text(fromUser,toUser,int(time.time()), content)
		elif msgType == 'image':
			try:
				#�õ�ϵͳ���ɵ�ͼƬ����
				picurl = xml.find('PicUrl').text
				datas = imgtest(picurl)
				return self.render.reply_text(fromUser, toUser, int(time.time()), ('ͼ�������Ա�Ϊ:'+datas[0]+'\n'+'����Ϊ:'+datas[1]).decode('gbk'))
			except:
				return self.render.reply_text(fromUser, toUser, int(time.time()), ('��ֻ��ʶ�����࣬�����˵���Ƭ�ͱ��ù�����').decode('gbk'))
		elif msgType == 'event':
			mscontent = xml.find("Event").text
			if mscontent == "subscribe":
				replayText = '��ӭ��ע��΢�ţ����΢���Ǳ���ҵ�మ����������Ҳ����һ��ѧϰPythonһ����Ķ���,���ڻ�û��ʲô���ܣ�ֻ������ʶ���ܣ��Ժ󻹻����Ŭ����'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
			if mscontent == "unsubscribe":
				replayText = '�����ڹ��ܻ��ܼ򵥣�֪�����㲻���������󣬵����һ������Ľ�����ӭ���Ժ�����'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
		else:
			pass
			