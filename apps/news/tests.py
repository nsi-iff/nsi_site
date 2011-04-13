#-*- coding:utf-8 -*-
from django.test import TestCase
from should_dsl import should
from apps.news.models import News


class TestNews(TestCase):

    def test_convert_its_RST_body_to_HTML(self):
        h = News(body="*NSI* site rulz!")
        h.body_as_html() |should| contain('<em>NSI</em> site rulz!')

