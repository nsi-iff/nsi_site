from django.shortcuts import render_to_response
from apps.members.models import Member

def show(request):
    member = Member.objects.all()[0]
    return render_to_response('show_member.html',
      { 'member': member})
