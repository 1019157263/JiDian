#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from creditHour import *
#from sunny import *
import time
'''
# 为线程定义一个函数
def job():
   from sunny import *
try:
   thread.start_new_thread(job, () )
except:
   print "Error: unable to start thread"
'''

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        data = {
            'kcmc_All': [
                ['请登录后再查看你的数据', '', ''],
            ],
            'computer_all': ['admin', '', '', ''],
            'HXkcmc_All': [
                ['请登录后再查看你的数据', '', ''],
            ],
            'HXkcmc_new': [
                ['请登录后再查看你的数据', '', ''],
            ],
            'HX_computer': ['admin', '', '', '']
        }

        self.render("temp/index.html",message="{{ message }}",userid="",info='{{ info }}',data=data)

    def post(self):
        username = self.get_argument('name')
        password = self.get_argument('pwd')
        print(username, password)
        a=data_super(username, password)
        print(a)
        self.render("temp/index.html", message="{{ message }}",userid=username,info='{{ info }}',data=a)


application = tornado.web.Application([
    (r"/index", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
