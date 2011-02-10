from django.shortcuts import render_to_response
from apps.teams.models import Team


def show_all(request):
    teams = Team.objects.all()
    return render_to_response('show_all.html',
      {'teams': teams,
       'team_count': len(teams)})
