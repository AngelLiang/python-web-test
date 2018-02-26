#!/bin/sh python
# coding=utf-8
# filename: gevent_flask.py

from gevent.wsgi import WSGIServer
from pure_flask import app

http_server = WSGIServer(('127.0.0.1', 8888), app)
http_server.serve_forever()
