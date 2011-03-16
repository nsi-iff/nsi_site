from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.tools.models import Tool


def show_all(request):
    tools = Tool.objects.all()
    return render_to_response(
        'show_all.html',
        {'tools': tools},
        context_instance=RequestContext(request)
    )
