from django.shortcuts import render_to_response
from apps.projects.models import Project


def show_all(request):
    projects = Project.objects.all()
    return render_to_response('show_all_projects.html',
      { 'projects': projects,
        'project_count': len(projects) })

def show_project(request, project_id):
    project = Project.objects.get(id=project_id)
    return render_to_response('show_project.html', { 'project': project })

