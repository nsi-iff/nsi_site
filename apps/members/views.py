from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.members.models import Member


def show_all_current_members(request):
    members = Member.objects.filter(is_renegade=False).order_by('function', 'started_nsi_date')
    return render_to_response(
        'show_all_current_members.html',
        {'members': members},
        context_instance=RequestContext(request)
    )

def show_member(request, slug):
    member = Member.objects.get(slug=slug)
    participation_list = member.participation_set.all()
    members = Member.objects.all()
    return render_to_response(
        'show_member.html',
        {'member': member, 'participation_list': participation_list, 'members': members},
        context_instance=RequestContext(request)
    )

def show_all_former_members(request):
    members = Member.objects.filter(is_renegade=True)
    return render_to_response(
        'show_all_former_members.html',
        {'members': members},
        context_instance=RequestContext(request)
    )
