from django.test import TestCase
from should_dsl import should
from model_mommy import mommy
from apps.members.models import Member


class MemberTest(TestCase):
    def test_github_link(self):
        m = mommy.make_one(Member, github="pluck", photo="ricks_sunshine.png", lattes=None, site=None)
        m.github_link() |should| equal_to("http://github.com/pluck")
        
    def test_twitter_link(self):
        m = mommy.make_one(Member, twitter="pluck", photo="ricks_sunshine.png", lattes=None, site=None)
        m.twitter_link() |should| equal_to("http://twitter.com/pluck")
        
    def test_slideshare_link(self):
        m = mommy.make_one(Member, slideshare="pluck", photo="ricks_sunshine.png", lattes=None, site=None)
        m.slideshare_link() |should| equal_to("http://www.slideshare.net/pluck")
