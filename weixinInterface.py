# -*- coding: utf-8 -*-
import hashlib
import web
import lxml.etree as etree
import time
import os
import random
from tulingAutoReply import TulingAutoReply
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
				replayText = '1.���� ����+���� ���ص���ĸó��е�����\n2.����m�������������������������м���ͣ����������������������wifi����(ƻ���ֻ����ṩ�Ĺ���)\n3.����ͼƬ ���Խ�������ʶ��\n4.����ʱ��+����+����+���� ���������人����ʯ�Ļ� ���͸�����Ʊ����\n5.����ͼƬ��Ϣ  ���͸�����ͼƬ����'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
			if content.lower().strip() == 'm':
				musicList = [
					[r'http://cdn.sinacloud.net/super3h/%E8%B5%B5%E9%9B%B7-%E6%88%90%E9%83%BD.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=Amv0p6bpTP','�ɶ�'.decode('gbk'),'һ�׹��ڳɶ�����ҥ'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E5%A5%87%E5%A6%99%E8%83%BD%E5%8A%9B%E6%AD%8C%20%E9%99%88%E7%B2%92.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=naNA%2BnoLeX','����������'.decode('gbk'),'������ô�������������ȴ����ס��'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E4%B8%83%E6%9C%88%E4%B8%8A.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=10lmgvWDSk','������'.decode('gbk'),'�����˷����ˣ��ྴ���꣬������ʶһ��'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E5%88%B0%E4%B8%8D%E4%BA%86.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=q5Uvmym2dp','������'.decode('gbk'),'���������.��������˱��˵� ����һ���ӱ��˻�����..���� ˭Ҳ�ܲ���'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E5%8D%97%E4%B8%8B.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=paaVSCLmSP','����'.decode('gbk'),'���������ˣ���֪������'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E5%8E%9F%E8%B0%85.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=JW7EyeexGp','����'.decode('gbk'),'������ů�ķ��� ���Ƕ�Ц�ú��� һ��ͣ����һ˲'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E5%91%8A%E7%99%BD%E6%B0%94%E7%90%83.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=HfJSFIkSy5','�������'.decode('gbk'),'��ϲ����Ta��װ�'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E6%88%91%E8%A6%81%E4%BD%A0.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=Jlr9j%2FzEX1','��Ҫ��'.decode('gbk'),'����Ҫ���ø�Բ�������� ��Ҫδ֪�ķ�� ��Ҫ��ɫ����� ����Ҫ�㡣'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E6%98%A5%E5%A4%8F%E7%A7%8B%E5%86%AC%E7%9A%84%E4%BD%A0.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=wgqRrlxCdY','�����ﶬ����'.decode('gbk'),'��ϲ�� ����Ļ� ������� ����Ļƻ� ��������� �� ÿ�����'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E7%88%B1%E6%83%85.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=%2B%2FTnudrYIP','����'.decode('gbk'),'������ĥ�˵Ķ���,ȴ���᲻����������'.decode('gbk')]
				
				]
				music = random.choice(musicList)
				musicurl = music[0]
				musictitle = music[1]
				musicdes = music[2]
				return self.render.reply_music(fromUser,toUser,int(time.time()),musictitle,musicdes,musicurl)
			if content == '����'.decode('gbk'):
				return self.render.reply_url(fromUser,toUser,int(time.time()),content,'���˲���'.decode('gbk'),'HHH�ĸ��˲���'.decode('gbk'),r'https://mmbiz.qlogo.cn/mmbiz_jpg/z67Nqg3yAzRNVazozLUD7icuibRJdnCDaJd1dTfQ9673IDS6ttA5cFQwQCic7IrjPhbTcX1ycQDGibJhlGaFbwzyyg/0?wx_fmt=jpeg',r'http://super3h.github.io')
			tuling = TulingAutoReply('b2091cea56054fc88d857baf3f926fbd',r'http://www.tuling123.com/openapi/api')
			replayText = tuling.reply(content)
			if isinstance(replayText,list):
				articleList = [article['article']+article['detailurl'] for article in articles]
				reply = random.choice(articleList)
				return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
			if replayText is None :
				replayText = '�Ͳ���˵���������Ļ�ô����'.decode('gbk')
			return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
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
				replayText = '��ӭ��ע��΢�ţ����΢���Ǳ���ҵ�మ����������Ҳ����һ��ѧϰPythonһ����Ķ���,������help�鿴���幦�ܣ����ܲ��࣬�Ժ󻹻����Ŭ����'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
			if mscontent == "unsubscribe":
				replayText = '�����ڹ��ܻ��ܼ򵥣�֪�����㲻���������󣬵����һ������Ľ�����ӭ���Ժ�����'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
		else:
			pass
			