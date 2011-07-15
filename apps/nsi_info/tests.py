from django.test import TestCase
from should_dsl import should
from apps.nsi_info.models import NSIInfo


class HistoryTest(TestCase):

    def test_convert_its_RST_text_to_HTML(self):
        h = NSIInfo(about="*NSI* site rulz!")
        h.about_as_html() |should| contain('<em>NSI</em> site rulz!')

