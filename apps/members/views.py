from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.members.models import Member


def show_all(request):
    members = Member.objects.all().order_by('function', 'started_nsi_date')
    return render_to_response(
        'show_all_members.html',
        {'members': members},
        context_instance=RequestContext(request)
    )

def show(request, member_id):
    member = Member.objects.get(id=member_id)
    participation_list = member.participation_set.all()
    members = Member.objects.all()
    return render_to_response(
        'show_member.html',
        {'member': member, 'participation_list': participation_list, 'members': members},
        context_instance=RequestContext(request)
    )
