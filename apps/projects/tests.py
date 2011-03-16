from django.test import TestCase
from should_dsl import should, should_not
from apps.projects.models import Project


class ProjectTest(TestCase):
    def test_finishing(self):
        project = Project(start_date='2011-01-01', end_date=None)
        project |should_not| be_finished
        project.end_date = '2011-01-31'
        project |should| be_finished
        
    def test_change_status_to_finished(self):
        project = Project(start_date='2011-01-01', end_date=None)
        project |should_not| be_finished
        project.end_date = '2011-01-31'
        project.save()
        project.status |should| equal_to('finalizado')
