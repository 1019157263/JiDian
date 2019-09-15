#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from creditHour import *


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("temp/index.html", info='')

    def post(self):
        username = self.get_argument('name')
        password = self.get_argument('pwd')
        print(username, password)
        data_super(username, password)


application = tornado.web.Application([
    (r"/index", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
