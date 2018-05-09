#!/bin/sh python
# coding=utf-8
# filename: pure_flask.py

from flask import Flask, render_template, make_response, jsonify

app = Flask(__name__)


@app.route('/')
def main_handler():
    return make_response("Hello World!")


@app.route('/template')
def template_handler():
    return render_template(
        'main_for_flask.html', messages="whatever", title="home", number=10000)


@app.route('/json')
def json_handler():
    return jsonify({"status": 1, "message": "OK", "data": {}})


if __name__ == '__main__':
    app.run(port=8888, debug=False)
