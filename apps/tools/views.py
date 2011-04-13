from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.tools.models import Tool


def show_tool(request, tool_id):
    tool = Tool.objects.get(id=tool_id)
    return render_to_response(
        'show_tool.html',
        {'tool': tool},
        context_instance=RequestContext(request)
    )

def show_all(request):
    tools = Tool.objects.all()
    return render_to_response(
        'show_all.html',
        {'tools': tools},
        context_instance=RequestContext(request)
    )
