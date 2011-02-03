from lettuce import step
from apps.history.models import History

@step(u'Given current history is "(.*)"')
def given_current_history_is_group1(step, history_text):
    History(text=history_text).save()

