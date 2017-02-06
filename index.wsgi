# coding: UTF-8
import sae#！！！


def application(environ, start_response):#！！！
    start_response('200 ok', [('content-type', 'text/plain')])#！！！
    return ['Hello, SAE!']

application=sae.create_wsgi_app(application)#！！！