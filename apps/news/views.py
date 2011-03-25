from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.news.models import News


def show_news(request):
    news = News.objects.all().order_by('-date_and_time')
    return render_to_response(
        'show_news.html',
        {'news': news},
        context_instance=RequestContext(request)
    )

def detail_news(request, news_id):
    news_obj = News.objects.get(id=news_id)
    return render_to_response(
        'detail_news.html',
        {'news_obj':news_obj},
        context_instance=RequestContext(request)
    )