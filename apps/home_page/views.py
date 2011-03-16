from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.news.models import News
from apps.projects.models import Project

def show_index(request):
    news = News.objects.all()
    projects = Project.objects.filter(status='aberto')
    return render_to_response(
        'index.html',
        {'news': news, 'projects': projects},
        context_instance=RequestContext(request)
    )
