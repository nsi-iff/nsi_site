# -*- coding: utf-8 -*-
from lettuce import step
from apps.members.models import Member

@step(u'Given exist a member:')
def given_exist_a_member(step):
    Member(**step.hashes[0]).save()

