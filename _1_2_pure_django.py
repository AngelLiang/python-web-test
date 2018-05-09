#!/bin/sh python
# coding=utf-8
# filename: pure_django.py

import sys
import json
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.core.wsgi import get_wsgi_application

settings.configure(
    DEBUG=True,
    SECRET_KEY='thesecret',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


def index(request):
    return HttpResponse('Hello World!')


def template_handle(request):
    pass


def json_handle(request):
    resp = {'statue': 1, 'message': 'OK', "data": {}}
    return HttpResponse(json.dumps(resp), content_type="application/json")


urlpatterns = (path("", index), path("template", template_handle),
               path("json", json_handle))

app = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    # execute_from_command_line(("runserver", 8888))
