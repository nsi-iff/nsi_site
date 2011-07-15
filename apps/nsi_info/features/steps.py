from lettuce import step
from apps.nsi_info.models import NSIInfo


@step(u'current about is "(.*)"')
def current_about_is(step, about_text):
    if len(NSIInfo.objects.all()) == 0:
        NSIInfo(about=about_text).save()
    else:
        info = NSIInfo.objects.all()[0]
        info.about = about_text
        info.save()

