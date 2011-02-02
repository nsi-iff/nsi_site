# -*- coding: utf-8 -*-
from lettuce import step
from teams.models import Team

@step(u'exist a team:')
def given_exist_a_team(step):
    Team(**step.hashes[0]).save()
