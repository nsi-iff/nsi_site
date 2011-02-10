from django.test import TestCase
from should_dsl import should
from apps.history.models import History


class HistoryTest(TestCase):

    def test_convert_its_RST_text_to_HTML(self):
        h = History(text="*NSI* site rulz!")
        h.to_html() |should| contain('<em>NSI</em> site rulz!')
