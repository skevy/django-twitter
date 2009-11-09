from django.utils.translation import ugettext_lazy as _
from django import forms
from models import TwitterAccount

class TwitterForm(forms.ModelForm):

    password = forms.CharField(label=_("Twitter Password"), required=True,
                               widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = TwitterAccount
