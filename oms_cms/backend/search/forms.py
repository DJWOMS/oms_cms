from django import forms
from django.utils.translation import gettext_lazy as _


class SearchForm(forms.Form):
    """Форма поиска"""
    q = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'placeholder': _('Поиск')})
    )
