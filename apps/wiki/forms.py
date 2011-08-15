from django.forms import ModelForm

from models import WikiItem


class WikiItemForm(ModelForm):

    class Meta:
        model = WikiItem
