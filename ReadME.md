# Python Web Test

Python Web框架测试集合，包括：

1. `pure_flask.py`：纯粹的 Flask
2. `pure_django.py`：纯粹的 Django2.0
3. `pure_tornado.py`：纯粹的 tornado
4. `gevent_flask.py`：基于 gevent 的 Flask
5. `gevent_django.py`：基于 gevent 的 Django2.0
6. `gevent_tornado.py`：基于 gevent 的 tornado
7. `gunicorn_flask.sh`：基于 gunicorn 的 Flask
8. `gunicorn_django.sh`：基于 gunicorn 的 Django2.0
9. `gunicorn_tornado.sh`：基于 gunicorn 的 tornado
10. `tornado_flask.py`：基于 tornado 的Flask

测试的Web框架版本和Python模块包（requirements.txt）：

Python版本：3.5.4

- Django==2.0.2
- Flask==0.12.2
- gevent==1.2.2
- gunicorn==19.7.1
- tornado==4.5.3
- eventlet==0.22.1
- aiohttp==3.0.3

requirements_pypy.txt 是给pypy使用。下面默认是使用CPython 3.5.4。

# 测试结果参考

- 测试配置：阿里云单核服务器
- 测试时间：2018年2月26日
- 测试命令：`ab -n 1000 -c 4 http://localhost:8888/` （发送1000个请求（-n 1000），每次发送4个请求（-c 4））

测试结论，在其他因素不变的情况下，只返回`Hello World`字符串，使用ab对各种Python Web框架进行压力测试，其性能从大到小为：

- gunicorn_django（1909.12）
- gunicorn_flask（1732.09）
- gevent_django（1710.94）
- gevent_flask（1572.45）
- gunicorn_tornado（1544.18）
- gunicorn_gevent_flask（1499.17）
- pure_flask（1474.66）
- gevent_tornado（1431.28）
- gunicorn_eventlet_flask（1383.50）
- pure_tornado（1328.77）
- pure_django（1076.35）

备注：

- 括号数值意义为ab的 Requests per second 测试数值。
- pure表示使用Web框架自带HTTP Server。
- gunicorn默认运行模式是`sync`，gunicorn_eventlet表示以`eventlet`模式运行。

