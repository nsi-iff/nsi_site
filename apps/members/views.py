from django.shortcuts import render_to_response
from apps.members.models import Member

def show(request, member_id):
    member = Member.objects.get(id=member_id)
    return render_to_response('show_member.html',
      { 'member': member})
