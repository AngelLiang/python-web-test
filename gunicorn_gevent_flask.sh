#!/bin/sh

venv/bin/gunicorn -b 127.0.0.1:8888 -k gevent pure_flask:app
