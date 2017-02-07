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
				replayText = '2.输入 book 要查询的书名 返回豆瓣图书中结果\n3.输入cls清除查询记录\n4.输入m随机来首音乐听，建议在wifi下听\n5.输入python 进入python常用模块用法查询（未完成）'.decode('gbk')
				return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
			if content.lower().strip() == 'm':
				musicList = [
					[r'http://cdn.sinacloud.net/super3h/%E8%B5%B5%E9%9B%B7-%E6%88%90%E9%83%BD.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=Amv0p6bpTP','成都'.decode('gbk'),'一首关于成都的民谣'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E5%A5%87%E5%A6%99%E8%83%BD%E5%8A%9B%E6%AD%8C%20%E9%99%88%E7%B2%92.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=naNA%2BnoLeX','奇妙能力歌'.decode('gbk'),'我有那么多奇妙的能力，却留不住你'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E4%B8%83%E6%9C%88%E4%B8%8A.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=10lmgvWDSk','七月上'.decode('gbk'),'我欲乘风破浪，相敬流年，不负相识一场'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E5%88%B0%E4%B8%8D%E4%BA%86.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=q5Uvmym2dp','到不了'.decode('gbk'),'心这个东西.如果先伤了别人的 总有一天会加倍伤回来的..放心 谁也跑不了'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E5%8D%97%E4%B8%8B.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=paaVSCLmSP','南下'.decode('gbk'),'生来北方人，不知江南心'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E5%8E%9F%E8%B0%85.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=JW7EyeexGp','房间'.decode('gbk'),'在这温暖的房间 我们都笑得很甜 一切停格在一瞬'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E5%91%8A%E7%99%BD%E6%B0%94%E7%90%83.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=HfJSFIkSy5','告白气球'.decode('gbk'),'想喜欢的Ta告白吧'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E6%88%91%E8%A6%81%E4%BD%A0.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=Jlr9j%2FzEX1','我要你'.decode('gbk'),'我想要更好更圆的月亮， 想要未知的疯狂， 想要声色的张扬， 我想要你。'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E6%98%A5%E5%A4%8F%E7%A7%8B%E5%86%AC%E7%9A%84%E4%BD%A0.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=wgqRrlxCdY','春夏秋冬的你'.decode('gbk'),'我喜欢 春天的花 夏天的树 秋天的黄昏 冬天的阳光 和 每天的你'.decode('gbk')],
					[r'http://cdn.sinacloud.net/super3h/%E7%88%B1%E6%83%85.mp3?KID=sina,2h52m0fNhoTzn5PApHvr&Expires=1486396834&ssig=%2B%2FTnudrYIP','爱情'.decode('gbk'),'爱是折磨人的东西,却又舍不得这样放弃'.decode('gbk')]
				
				]
				music = random.choice(musicList)
				musicurl = music[0]
				musictitle = music[1]
				musicdes = music[2]
				return self.render.reply_music(fromUser,toUser,int(time.time()),musictitle,musicdes,musicurl)
			tuling = TulingAutoReply('b2091cea56054fc88d857baf3f926fbd',r'http://www.tuling123.com/openapi/api')
			replayText = tuling.reply(content)
			if replayText is None :
				replayText = '就不能说点能听懂的话么？？'.decode('gbk')
			elif isinstance(replayText, list):
				reply = ''
				for article in replayText:
					reply += '\n'
					reply = reply+article['article']+'\n详情：'.decode('gbk')+article['detailurl']
				return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
			return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
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
			