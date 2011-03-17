from lettuce import step
from model_mommy.mommy import Mommy
from apps.projects.models import Project
from apps.tools.models import Tool

@step(u'exist a tool:')
def there_exist_a_tool(step):
    for tool_hashes in step.hashes:
        Tool.objects.create(**tool_hashes)        

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
