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
				musicList = [
					[r'http://super3h.bj.bcebos.com/%E8%B5%B5%E9%9B%B7-%E6%88%90%E9%83%BD.mp3','�ɶ�'.decode('gbk'),'һ�׹��ڳɶ�����ҥ'.decode('gbk')],
					[r'http://super3h.bj.bcebos.com/%E5%A5%87%E5%A6%99%E8%83%BD%E5%8A%9B%E6%AD%8C%20%E9%99%88%E7%B2%92.mp3','����������'.decode('gbk'),'������ô�������������ȴ����ס��'.decode('gbk')]
				
				]
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
			