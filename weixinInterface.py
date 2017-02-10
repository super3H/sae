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
				replayText = '1.输入 天气+城市 返回当天的该城市的天气\n2.输入m随机来首音乐听，！！！点击中间暂停键即可收听！！！建议在wifi下听(苹果手机不提供改功能)\n3.发送图片 可以进行人脸识别\n4.输入时间+城市+城市+工具 例如明天武汉到黄石的火车 发送给您购票链接\n5.输入图片信息  发送给您的图片链接\n6.输入新闻，发送今天相关的新闻\n7.输入博客，可以访问我的个人博客'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
			if content.lower().strip() == 'm':
				musicList = [
					[r'http://sz-btfs.ftn.qq.com/ftn_handler/2cc23e8dafb31c35363a3c39e900dd9fe5c235b50762faf1b49705d267d422678ddad67f258f3752bcc4653324d9390e532079cb42c84711fbae78da7d3bbe54/%E8%B5%B5%E9%9B%B7-%E6%88%90%E9%83%BD.mp3','成都'.decode('gbk'),'一首关于成都的民谣'.decode('gbk')],
					[r'http://sz-ctfs.ftn.qq.com/ftn_handler/7b58ec7a523887d4d9284f234a4d0061c64771af32b95f2dfbc61b12a1c514881e119bab54f60c136fab41934676f70438741bc3d72216ab9bbad5267c65bd92/%E5%A5%87%E5%A6%99%E8%83%BD%E5%8A%9B%E6%AD%8C%20%E9%99%88%E7%B2%92.mp3','奇妙能力歌'.decode('gbk'),'我有那么多奇妙的能力，却留不住你'.decode('gbk')],
					[r'http://sz-btfs.ftn.qq.com/ftn_handler/648b012faa45729a791d71cc18814ff10d4a68a1bc01b3124d6375d5491e7caacc2074a5da08f2cbca9efd32f520f1b709dc241d5cb197a3db1557f0fe5fd7ec/?fname=%E4%B8%83%E6%9C%88%E4%B8%8A.mp3','七月上'.decode('gbk'),'我欲乘风破浪，相敬流年，不负相识一场'.decode('gbk')],
					[r'http://sh-btfs.ftn.qq.com/ftn_handler/bac6bdd51934a94c90dadcb4301dcb65f83c599d7d41b3ab5709397d1f03724701f7ef0ffbcde9deec7e771b736de5365432d05b6b18c690f3081abf83ba2f5f/%E5%88%B0%E4%B8%8D%E4%BA%86.mp3','到不了'.decode('gbk'),'心这个东西.如果先伤了别人的 总有一天会加倍伤回来的..放心 谁也跑不了'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/a0f18ebed344549f629d1a838b8fe6ed0d163a7336e195991fc0ad9a688a59ea2ca9b848cd122a5b3102b2c68b559cdb37d229777165520db5e8f1a8f5d16657/%E5%8D%97%E4%B8%8B.mp3','南下'.decode('gbk'),'生来北方人，不知江南心'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/c47cedaa54f1624a6b7c8e942b9e0bd1b75e78d8768c973d917ee79035f61a5fb2da4b187a5e42aa142e6b52f3648916793ec04197b9626139c4f35dd2c0d502/%E6%88%BF%E9%97%B4.mp3','房间'.decode('gbk'),'在这温暖的房间 我们都笑得很甜 一切停格在一瞬'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/929758c4e674b77f31eacd501125be223cab72f4f7799154cfcb99b2935f17833854aad7675a871ad1e2943b2c56a788d2a46e8126b462abf446e61bf4961ec6/%E5%91%8A%E7%99%BD%E6%B0%94%E7%90%83.mp3','告白气球'.decode('gbk'),'向喜欢的Ta告白吧'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/a929de2e9ad0301d8fbe153f573ecb80e02e0e82d6da7ef1468c6f3cd1da3699a19068a0a3e3e5aeaf902622a12a615ca211eccf98f8e3fb4433480aeed0692c/%E6%88%91%E8%A6%81%E4%BD%A0.mp3','我要你'.decode('gbk'),'我想要更好更圆的月亮， 想要未知的疯狂， 想要声色的张扬， 我想要你。'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/fe4aead7483bb2dda36488796938aa25541d45a5102c0740372dc4f45659b10332c3baf1a08918eca22cc4234fc646a384a4e8e5aa715a23ff4177ea8f8f629d/%E6%98%A5%E5%A4%8F%E7%A7%8B%E5%86%AC%E7%9A%84%E4%BD%A0.mp3','春夏秋冬的你'.decode('gbk'),'我喜欢 春天的花 夏天的树 秋天的黄昏 冬天的阳光 和 每天的你'.decode('gbk')],
					[r'http://sh-ctfs.ftn.qq.com/ftn_handler/c26f1616ce6d42e98bb44053500b34ce831ebfd768d67a65a2229dc90a3af6539d65adc70bf66609d26b01215b0b0c099d2f4735a54b82fbc01187d50238e3d1/%E7%88%B1%E6%83%85.mp3','爱情'.decode('gbk'),'爱是折磨人的东西,却又舍不得这样放弃'.decode('gbk')]
				
				]
				music = random.choice(musicList)
				musicurl = music[0]
				musictitle = music[1]
				musicdes = music[2]
				return self.render.reply_music(fromUser,toUser,int(time.time()),musictitle,musicdes,musicurl)
			if content == '博客'.decode('gbk'):
				return self.render.reply_url(fromUser,toUser,int(time.time()),content,'个人博客'.decode('gbk'),'HHH的个人博客'.decode('gbk'),r'https://mmbiz.qlogo.cn/mmbiz_jpg/z67Nqg3yAzRNVazozLUD7icuibRJdnCDaJd1dTfQ9673IDS6ttA5cFQwQCic7IrjPhbTcX1ycQDGibJhlGaFbwzyyg/0?wx_fmt=jpeg',r'http://super3h.github.io')
			tuling = TulingAutoReply('b2091cea56054fc88d857baf3f926fbd',r'http://www.tuling123.com/openapi/api')
			replayText = tuling.reply(content)
			if isinstance(replayText,list):
				articleList = [article['article']+'\n详情'.decode('gbk')+article['detailurl'] for article in replayText]
				reply = random.choice(articleList)
				return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
			if replayText is None :
				replayText = '就不能说点能听懂的话么？？'.decode('gbk')
			return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
		elif msgType == 'image':
			try:
				#拿到系统生成的图片链接
				picurl = xml.find('PicUrl').text
				datas = imgtest(picurl)
				return self.render.reply_text(fromUser, toUser, int(time.time()), ('图中人物性别为:'+datas[0]+'\n'+'年龄为:'+datas[1]).decode('gbk'))
			except:
				return self.render.reply_text(fromUser, toUser, int(time.time()), ('我只能识别人类，不是人的照片就别拿过来了').decode('gbk'))
		else:
			return self.render.reply_text(fromUser, toUser, int(time.time()), ('功能只有这么多，能力有限，不好意思').decode('gbk'))
			