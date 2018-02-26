#!/bin/sh python
# coding=utf-8
# filename: gevent_flask.py

from gevent.wsgi import WSGIServer
from pure_django import app

http_server = WSGIServer(('', 8888), app)
http_server.serve_forever()
