from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.news.models import News
from apps.projects.models import Project


def show_news(request):
    news = News.objects.all()
    return render_to_response(
        'show_news.html',
        {'news': news},
        context_instance=RequestContext(request)
    )
