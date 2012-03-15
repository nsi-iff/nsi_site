from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.news.models import News
from apps.projects.models import Project
from apps.tools.models import Tool

def show_index(request):
    news = News.objects.all()[:3]
    projects = Project.objects.filter(status='aberto')
    tools = Tool.objects.filter(highlight=True)

    return render_to_response(
        'index.html',
        {'news': news, 'projects': projects, 'tools': tools},
        context_instance=RequestContext(request)
    )
