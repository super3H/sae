# coding:utf-8
import json
import requests
import traceback
 
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
			# �ı���
            if js['code'] == 100000:
                return js['text']
			# ������
            elif js['code'] == 302000:
                return js['list']
        except Exception:
            traceback.print_exc()
            return None