# -*- coding: utf-8 -*-
import hashlib
import web
import lxml.etree as etree
import time
import os
import random
from imgtest import imgtest
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
					[r'http://collegeshare.oss-cn-qingdao.aliyuncs.com/weixin/music/%E8%B5%B5%E9%9B%B7%20-%20%E6%88%90%E9%83%BD.mp3','成都'.decode('gbk'),'一首关于成都的民谣'.decode('gbk')],
					[r'http://collegeshare.oss-cn-qingdao.aliyuncs.com/weixin/music/%E5%A5%87%E5%A6%99%E8%83%BD%E5%8A%9B%E6%AD%8C%20%E9%99%88%E7%B2%92.mp3','奇妙能力歌'.decode('gbk'),'我有那么多奇妙的能力，却留不住你'.decode('gbk')],
					[r'http://collegeshare.oss-cn-qingdao.aliyuncs.com/weixin/music/%E4%B8%83%E6%9C%88%E4%B8%8A%20-%20Jam.mp3','七月上'.decode('gbk'),'我欲乘风破浪，相敬流年，不负相识一场'.decode('gbk')],
					[r'http://collegeshare.oss-cn-qingdao.aliyuncs.com/weixin/music/%E6%9D%8E%E4%BB%A3%E6%B2%AB%20-%20%E5%88%B0%E4%B8%8D%E4%BA%86.mp3','到不了'.decode('gbk'),'心这个东西.如果先伤了别人的 总有一天会加倍伤回来的..放心 谁也跑不了'.decode('gbk')],
					[r'http://collegeshare.oss-cn-qingdao.aliyuncs.com/weixin/music/%E5%BE%90%E6%B5%B7%E4%BF%8F%20-%20%E5%8D%97%E4%B8%8B.mp3','南下'.decode('gbk'),'生来北方人，不知江南心'.decode('gbk')],
					[r'http://collegeshare.oss-cn-qingdao.aliyuncs.com/weixin/music/%E5%88%98%E7%91%9E%E7%90%A6%20-%20%E6%88%BF%E9%97%B4.mp3','房间'.decode('gbk'),'在这温暖的房间 我们都笑得很甜 一切停格在一瞬'.decode('gbk')],
					[r'http://collegeshare.oss-cn-qingdao.aliyuncs.com/weixin/music/%E4%B8%87%E5%B2%81%E7%88%BA%20-%20%E7%88%B1%E6%83%85.mp3','告白气球'.decode('gbk'),'向喜欢的Ta告白吧'.decode('gbk')],
					[r'http://collegeshare.oss-cn-qingdao.aliyuncs.com/weixin/music/%E4%BB%BB%E7%B4%A0%E6%B1%90%20-%20%E6%88%91%E8%A6%81%E4%BD%A0.mp3','我要你'.decode('gbk'),'我想要更好更圆的月亮， 想要未知的疯狂， 想要声色的张扬， 我想要你。'.decode('gbk')],
					[r'http://collegeshare.oss-cn-qingdao.aliyuncs.com/weixin/music/%E7%8E%8B%E5%AE%87%E8%89%AF%2B-%2B%E6%98%A5%E5%A4%8F%E7%A7%8B%E5%86%AC%E7%9A%84%E4%BD%A0.mp3','春夏秋冬的你'.decode('gbk'),'我喜欢 春天的花 夏天的树 秋天的黄昏 冬天的阳光 和 每天的你'.decode('gbk')],
					[r'http://collegeshare.oss-cn-qingdao.aliyuncs.com/weixin/music/%E4%B8%87%E5%B2%81%E7%88%BA%20-%20%E7%88%B1%E6%83%85.mp3','爱情'.decode('gbk'),'爱是折磨人的东西,却又舍不得这样放弃'.decode('gbk')]
				
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
			