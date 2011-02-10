# -*- coding: utf-8 -*-
from lettuce import step, world
from apps.members.models import Member
from lettuce.django import django_url
from apps.teams.models import Team

@step(u'Given exist a team:')
def given_exist_a_team(step):
    Team(**step.hashes[0]).save()

@step(u'And "(.*)" team has the member:')
def and_team_has_the_member(step, team_name):
    team = Team.objects.get(name=team_name)
    member = Member.objects.create(**step.hashes[0])
#    member.save()
    member.current_team.add(team)
    member.save()
    
@step(r'I go to the "(.+)" member page')
def i_go_to_member_page(step, member_name):
    member_obj = Member.objects.get(name=member_name)
    world.browser.visit(django_url('/member/%i' % member_obj.id))

