from django.test import TestCase
from should_dsl import should, should_not
from model_mommy import mommy
from projects.models import Project

class ProjectTest(TestCase):
    def test_finishing(self):
        project = mommy.make_one(Project, logo=None,
            start_date='2011-01-01', end_date=None)
        project |should_not| be_finished
        project.end_date = '2011-01-31'
        project |should| be_finished

