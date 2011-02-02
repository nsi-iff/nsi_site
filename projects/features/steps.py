from lettuce import step
from projects.models import Project

@step(u'Given exist a project:')
def given_exist_a_project(step):
    Project(**step.hashes[0]).save()

