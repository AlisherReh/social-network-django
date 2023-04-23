from django import forms
from .models import Status

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['bio', 'country', 'phone', 'profile_picture']
        