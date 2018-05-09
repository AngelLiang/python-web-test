# coding=utf-8

from apistar import Include, Route, App


def hello():
    return "Hello World!"


routes = [
    Route('/', 'GET', hello),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
