from django import forms

from .models import Feedback


class FeedbackFullForm(forms.ModelForm):
    """Форма обратной связи"""
    class Meta:
        model = Feedback
        fields = ("full_name", "email", "phone", "subject", "message")

