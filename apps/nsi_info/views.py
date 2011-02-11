from django.shortcuts import render_to_response
from apps.nsi_info.models import NSIInfo


def show_history(request):
    return render_to_response('show_history.html',
      {'nsi_info': NSIInfo.objects.all()[0]})


def show_summary(request):
    return render_to_response('show_summary.html',
      {'nsi_info': NSIInfo.objects.all()[0]})

