from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.nsi_info.models import NSIInfo


def show_history(request):
    if len(NSIInfo.objects.all()):
        nsi_info = NSIInfo.objects.latest('updated_at')
    else:
        nsi_info = list()
    return render_to_response(
        'show_history.html',
        {'nsi_info': nsi_info},
        context_instance=RequestContext(request)
    )


def show_summary(request):
    if len(NSIInfo.objects.all()):
        nsi_info = NSIInfo.objects.latest('updated_at')
    else:
        nsi_info = list()
    return render_to_response(
        'show_summary.html',
        {'nsi_info': nsi_info},
        context_instance=RequestContext(request)
    )

