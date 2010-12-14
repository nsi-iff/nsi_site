from django.shortcuts import render_to_response
from forms import ProjectForm
from models import Project

def new_project(request):
    project_form = ProjectForm()
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)        
        if project_form.is_valid():
            project = project_form.save()
            return render_to_response(
                'project_saved.html',
                {'project': project}
            )
    return render_to_response(
        'edit_project.html',
        {'project_form': project_form}
    )

def update_project(request, project_name):
    project = Project.objects.get(name=project_name)
    project_form = ProjectForm(instance=project)
    if request.method == 'POST':
        project_form = ProjectForm(request.POST,instance=project)        
        if project_form.is_valid():
            project = project_form.save()
            return render_to_response(
                'project_saved.html',
                {'project': project}
            )
    return render_to_response(
        'edit_project.html',
        {'project_form': project_form}
    )