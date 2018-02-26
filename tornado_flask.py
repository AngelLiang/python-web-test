#!/bin/sh python
# coding=utf-8
# filename: tornado_flask.py.py

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from pure_flask import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8888)
IOLoop.instance().start()
