from django.shortcuts import render_to_response
from apps.news.models import New
from apps.projects.models import Project

def show_news(request):
    news = New.objects.all()
    return render_to_response(
        'show_news.html',
        {'news': news},
    )
