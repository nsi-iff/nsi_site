from django.shortcuts import render_to_response
from apps.members.models import Member


def show_all(request):
    members = Member.objects.all()
    return render_to_response(
        'show_all_members.html',
        {'members': members},
    )

def show(request, member_id):
    member = Member.objects.get(id=member_id)
    participation_list = member.participation_set.all()
    return render_to_response(
        'show_member.html',
        {'member': member, 'participation_list': participation_list},
    )
