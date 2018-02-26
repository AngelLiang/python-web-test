#!/bin/sh
# gunicorn -k eventlet

venv/bin/gunicorn -b 127.0.0.1:8888 -k eventlet pure_flask:app
