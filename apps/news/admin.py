#!/usr/bin/env python
# encoding: utf-8
from django.contrib.admin import site

from apps.news.models import News

site.register(News)
