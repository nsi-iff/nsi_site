import os
import shutil
from django.conf import settings
from lettuce import step, world
from apps.projects.models import Project

@step(u'Given exist a project:')
def given_exist_a_project(step):
    Project(**step.hashes[0]).save()
    file_name = step.hashes[0]['logo'].split('/')[-1]
    shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'projects',
                              'features', 'resources', file_name),
                 os.path.join(settings.MEDIA_ROOT, 'images', 'projects'))

