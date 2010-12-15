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

def delete_project(request, project_name):
    project = Project.objects.get(name=project_name)
    if request.method == 'POST':
        project_id = request.POST.get('project_id', None)
        if project_id is not None:
            project = Project.objects.get(id=project_id)
            project.delete()
            return render_to_response('project_deleted.html')
    return render_to_response(
        'delete_project.html',
        {'project':project},
    )