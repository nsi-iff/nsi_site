import os
import shutil
from datetime import datetime
from django.conf import settings
from lettuce import step, world
from apps.projects.models import Project, Document

@step(u'exist a project:')
def given_exist_a_project(step):
    Project(**step.hashes[0]).save()
    file_name = step.hashes[0]['logo'].split('/')[-1]
    shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'projects',
                              'features', 'resources', file_name),
                 os.path.join(settings.MEDIA_ROOT, 'images', 'projects'))

@step(u'"(.*)" project has attached the following documents:')
def project_has_attached_the_following_documents(step, project_name):
    project = Project.objects.get(name=project_name)
    document = Document(**step.hashes[0])
    document.project = project
    document.save()

