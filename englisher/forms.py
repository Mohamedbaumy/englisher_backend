from django import forms
from .models import Email, Mail


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = "__all__"
