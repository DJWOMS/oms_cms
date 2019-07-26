from django import forms
from .models import Comments


class CommentsForm(forms.ModelForm):
    """Форма добавления комментария"""

    class Meta:
        model = Comments
        fields = ("text", )
