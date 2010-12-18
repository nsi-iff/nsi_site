from django.shortcuts import render_to_response
from forms import NewsForm
from models import News

def new_news(request):
    news_form = NewsForm()
    if request.method == 'POST':
        news_form = NewsForm(request.POST, request.FILES)
        if news_form.is_valid():
            news = news_form.save()
            return render_to_response(
                'news_saved.html',
                {'news': news}
            )
    return render_to_response(
        'edit_news.html',
        {'news_form': news_form}
    )

def update_news(request, news_title):
    news = News.objects.get(title=news_title)
    news_form = NewsForm(instance=news)
    if request.method == 'POST':
        news_form = NewsForm(request.POST, request.FILES)
        if news_form.is_valid():
            news = news_form.save()
            return render_to_response(
                'news_saved.html',
                {'news': news}
            )
    return render_to_response(
        'edit_news.html',
        {'news_form': news_form}
    )

def delete_news(request, news_title):
    news = News.objects.get(title=news_title)
    if request.method == 'POST':
        news_id = request.POST.get('news_id', None)
        if news_id is not None:
            news = News.objects.get(id=news_id)
            news.delete()
            return render_to_response('news_deleted.html')
    return render_to_response(
        'delete_news.html',
        {'news':news},
    )

