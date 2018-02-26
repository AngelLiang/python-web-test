#!/bin/sh python
# coding=utf-8
# filename: pure_tornado.py.py

import os.path
import tornado.wsgi
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")


class TemplateHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'main.html',
            page_title="",
            body_id="",
            messages="whatever",
            title="home",
            number=10000)


class JsonHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish({'message': 'ok'})


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), 'static'),
    "template_path": "templates",
}
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/template", TemplateHandler),
    (r"/json", JsonHandler),
], **settings)

app = tornado.wsgi.WSGIAdapter(application)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
