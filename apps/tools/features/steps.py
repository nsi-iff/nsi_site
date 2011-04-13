import os
import shutil
from lettuce import step
from model_mommy.mommy import Mommy
from apps.projects.models import Project
from apps.tools.models import Tool

@step(u'exist a tool:')
def there_exist_a_tool(step):
    for tool_hashes in step.hashes:
        Tool.objects.create(**tool_hashes)  
        if tool_hashes.get('logo'):
          file_name = tool_hashes['logo'].split('/')[-1]
          shutil.copy2(os.path.join(settings.PROJECT_ROOT_PATH, 'apps', 'tools',
                                  'features', 'resources', file_name),
                     os.path.join(settings.MEDIA_ROOT, 'test', 'images', 'tools'))      

@step(u'exist a project:')
def exist_a_project(step):
    for project_hashes in step.hashes:
        mom = Mommy(Project, False)
        project = mom.make_one(name=project_hashes.get('name'))
        
        
@step(u'And "(.*)" has related projects:')
def and_tool_has_related_projects(step, tool_name):
    tool = Tool.objects.get(name=tool_name)
    for project_hashes in step.hashes:
        project = Project.objects.get(name=project_hashes.get('name'))
        tool.relateds_projects.add(project)
    tool.save()
    
    
@step(r'I go to the "(.+)" tool page')
def i_go_to_tool_page(step, tool_name):
    tool_obj = Tool.objects.get(name=tool_name)
    world.browser.visit(django_url('/ferramenta/%i' % tool_obj.id))
