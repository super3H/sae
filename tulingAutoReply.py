# coding:utf-8
import json
import requests
import traceback
from random import choice 
class TulingAutoReply:
    def __init__(self, tuling_key, tuling_url):
        self.key = tuling_key
        self.url = tuling_url
 
    def reply(self, reply):
        body = {'key': self.key, 'info': reply}
        r = requests.post(self.url, data=body)
        #设置编码
        r.encoding = 'utf-8'
        resp = r.text
        if resp is None or len(resp) == 0:
            return None
        try:
            js = json.loads(resp)
			# 回复为文本类
            if js['code'] == 100000:
                return js['text']
			# 回复为链接类
            elif js['code'] == 200000:
                return js['url']
			# 回复为新闻类
            elif js['code'] == 302000:
			    return j['text']+j['list'][0]['info']+j['list'][0]['detailurl']
			# 其他
            else:
                return None
        except Exception:
            traceback.print_exc()
            return None