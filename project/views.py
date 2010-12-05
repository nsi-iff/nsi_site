from django.shortcuts import render_to_response
from forms import ProjectForm

def new_project(request):
    project_form = ProjectForm()
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)        
        if project_form.is_valid():
            project = project_form.save()
            project.save()
            return render_to_response(
                'project_saved.html',
                {'project': project}
            )
    return render_to_response(
        'new_project.html',
        {'project_form': project_form}
    )
