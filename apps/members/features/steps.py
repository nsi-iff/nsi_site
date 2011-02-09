# -*- coding: utf-8 -*-
from lettuce import step, world
from apps.members.models import Member
from lettuce.django import django_url

@step(u'Given exist a member:')
def given_exist_a_member(step):
    Member(**step.hashes[0]).save()
    
@step(r'I go to the "(.+)" member page')
def i_go_to_member_page(step, member_name):
    member_obj = Member.objects.get(name=member_name)
    world.browser.visit(django_url('/member/%i' % member_obj.id))

