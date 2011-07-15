from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.nsi_info.models import NSIInfo


def show_about(request):
    if len(NSIInfo.objects.all()):
        nsi_info = NSIInfo.objects.latest('updated_at')
    else:
        nsi_info = list()
    return render_to_response(
        'show_about.html',
        {'nsi_info': nsi_info},
        context_instance=RequestContext(request)
    )
