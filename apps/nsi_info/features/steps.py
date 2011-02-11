from lettuce import step
from apps.nsi_info.models import NSIInfo


@step(u'current history is "(.*)"')
def current_history_is(step, history_text):
    if len(NSIInfo.objects.all()) == 0:
        NSIInfo(history=history_text, summary='spam').save()
    else:
        info = NSIInfo.objects.all()[0]
        info.history = history_text
        info.save()


@step(u'current summary is "(.*)"')
def current_summary_is(step, summary_text):
    if len(NSIInfo.objects.all()) == 0:
        NSIInfo(history='eggs', summary=summary_text).save()
    else:
        info = NSIInfo.objects.all()[0]
        info.summary = summary_text
        info.save()

