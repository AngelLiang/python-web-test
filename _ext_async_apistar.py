# coding=utf-8

from apistar import Include, Route, ASyncApp


async def hello() -> str:
    return "Hello World!"


routes = [
    Route('/', 'GET', hello),
]

app = ASyncApp(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 8888, debug=True)
