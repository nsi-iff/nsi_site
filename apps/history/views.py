from django.shortcuts import render_to_response
from apps.history.models import History


def show(request):
    return render_to_response('show.html',
      {'history': History.objects.all()[0]})
