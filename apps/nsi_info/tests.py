from django.test import TestCase
from should_dsl import should
from apps.nsi_info.models import NSIInfo


class HistoryTest(TestCase):

    def test_convert_its_RST_text_to_HTML(self):
        h = NSIInfo(history="*NSI* site rulz!", summary="Site *NSI* sinistro!")
        h.history_as_html() |should| contain('<em>NSI</em> site rulz!')
        h.summary_as_html() |should| contain('Site <em>NSI</em> sinistro!')

