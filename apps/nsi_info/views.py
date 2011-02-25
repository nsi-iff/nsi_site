from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.nsi_info.models import NSIInfo


def show_history(request):
    return render_to_response(
        'show_history.html',
        {'nsi_info': NSIInfo.objects.all()[0]},
        context_instance=RequestContext(request)
    )


def show_summary(request):
    return render_to_response(
        'show_summary.html',
        {'nsi_info': NSIInfo.objects.all()[0]},
        context_instance=RequestContext(request)
    )

