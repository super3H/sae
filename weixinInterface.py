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
				replayText = '1.���� ����+���� ���ص���ĸó��е�����\n2.����m�������������������������м���ͣ����������������������wifi����(ƻ���ֻ����ṩ�Ĺ���)\n3.����ͼƬ ���Խ�������ʶ��\n4.����ʱ��+����+����+���� ���������人����ʯ�Ļ� ���͸�����Ʊ����\n5.����ͼƬ��Ϣ  ���͸�����ͼƬ����\n6.�������ţ����ͽ�����ص�����\n7.���벩�ͣ����Է����ҵĸ��˲���'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
			if content.lower().strip() == 'm':
				musicList = [
					[r'http://sz-btfs.ftn.qq.com/ftn_handler/2cc23e8dafb31c35363a3c39e900dd9fe5c235b50762faf1b49705d267d422678ddad67f258f3752bcc4653324d9390e532079cb42c84711fbae78da7d3bbe54/%E8%B5%B5%E9%9B%B7-%E6%88%90%E9%83%BD.mp3','�ɶ�'.decode('gbk'),'һ�׹��ڳɶ�����ҥ'.decode('gbk')],
					[r'http://sz-ctfs.ftn.qq.com/ftn_handler/7b58ec7a523887d4d9284f234a4d0061c64771af32b95f2dfbc61b12a1c514881e119bab54f60c136fab41934676f70438741bc3d72216ab9bbad5267c65bd92/%E5%A5%87%E5%A6%99%E8%83%BD%E5%8A%9B%E6%AD%8C%20%E9%99%88%E7%B2%92.mp3','����������'.decode('gbk'),'������ô�������������ȴ����ס��'.decode('gbk')],
					[r'http://sz-btfs.ftn.qq.com/ftn_handler/648b012faa45729a791d71cc18814ff10d4a68a1bc01b3124d6375d5491e7caacc2074a5da08f2cbca9efd32f520f1b709dc241d5cb197a3db1557f0fe5fd7ec/?fname=%E4%B8%83%E6%9C%88%E4%B8%8A.mp3','������'.decode('gbk'),'�����˷����ˣ��ྴ���꣬������ʶһ��'.decode('gbk')],
					[r'http://sh-btfs.ftn.qq.com/ftn_handler/bac6bdd51934a94c90dadcb4301dcb65f83c599d7d41b3ab5709397d1f03724701f7ef0ffbcde9deec7e771b736de5365432d05b6b18c690f3081abf83ba2f5f/%E5%88%B0%E4%B8%8D%E4%BA%86.mp3','������'.decode('gbk'),'���������.��������˱��˵� ����һ���ӱ��˻�����..���� ˭Ҳ�ܲ���'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/a0f18ebed344549f629d1a838b8fe6ed0d163a7336e195991fc0ad9a688a59ea2ca9b848cd122a5b3102b2c68b559cdb37d229777165520db5e8f1a8f5d16657/%E5%8D%97%E4%B8%8B.mp3','����'.decode('gbk'),'���������ˣ���֪������'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/c47cedaa54f1624a6b7c8e942b9e0bd1b75e78d8768c973d917ee79035f61a5fb2da4b187a5e42aa142e6b52f3648916793ec04197b9626139c4f35dd2c0d502/%E6%88%BF%E9%97%B4.mp3','����'.decode('gbk'),'������ů�ķ��� ���Ƕ�Ц�ú��� һ��ͣ����һ˲'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/929758c4e674b77f31eacd501125be223cab72f4f7799154cfcb99b2935f17833854aad7675a871ad1e2943b2c56a788d2a46e8126b462abf446e61bf4961ec6/%E5%91%8A%E7%99%BD%E6%B0%94%E7%90%83.mp3','�������'.decode('gbk'),'��ϲ����Ta��װ�'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/a929de2e9ad0301d8fbe153f573ecb80e02e0e82d6da7ef1468c6f3cd1da3699a19068a0a3e3e5aeaf902622a12a615ca211eccf98f8e3fb4433480aeed0692c/%E6%88%91%E8%A6%81%E4%BD%A0.mp3','��Ҫ��'.decode('gbk'),'����Ҫ���ø�Բ�������� ��Ҫδ֪�ķ�� ��Ҫ��ɫ����� ����Ҫ�㡣'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/fe4aead7483bb2dda36488796938aa25541d45a5102c0740372dc4f45659b10332c3baf1a08918eca22cc4234fc646a384a4e8e5aa715a23ff4177ea8f8f629d/%E6%98%A5%E5%A4%8F%E7%A7%8B%E5%86%AC%E7%9A%84%E4%BD%A0.mp3','�����ﶬ����'.decode('gbk'),'��ϲ�� ����Ļ� ������� ����Ļƻ� ��������� �� ÿ�����'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/c26f1616ce6d42e98bb44053500b34ce831ebfd768d67a65a2229dc90a3af6539d65adc70bf66609d26b01215b0b0c099d2f4735a54b82fbc01187d50238e3d1/%E7%88%B1%E6%83%85.mp3','����'.decode('gbk'),'������ĥ�˵Ķ���,ȴ���᲻����������'.decode('gbk')]
				
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
				articleList = [article['article']+'\n����'.decode('gbk')+article['detailurl'] for article in replayText]
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
		else:
			return self.render.reply_text(fromUser, toUser, int(time.time()), ('����ֻ����ô�࣬�������ޣ�������˼').decode('gbk'))
			