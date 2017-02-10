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
        #���ñ���
        r.encoding = 'utf-8'
        resp = r.text
        if resp is None or len(resp) == 0:
            return None
        try:
            js = json.loads(resp)
			# �ظ�Ϊ�ı���
            if js['code'] == 100000:
                return js['text']
			# �ظ�Ϊ������
            elif js['code'] == 200000:
                return js['url']
            elif js['code'] == 302000:
			    articles = js['list']
                articleList = [article['article']+article['detailurl'] for article in articles ]
                return choice(articleList)
			# ����
            else:
                return None
        except Exception:
            traceback.print_exc()
            return None