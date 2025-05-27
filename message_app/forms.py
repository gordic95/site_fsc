from django import forms
from . models import Message
from django.utils.translation import gettext_lazy as _


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('author_from', 'author_to', 'message')
