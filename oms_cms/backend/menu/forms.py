from django import forms
from .models import MenuItem
from .widgets import GfkLookupWidget


class MenuItemAdminForm(forms.ModelForm):
    """Форма пунктов меню админ панели"""
    class Meta(object):
        model = MenuItem
        fields = ('__all__')
        exclude = ("slug",)
        widgets = {
            'object_id': GfkLookupWidget(
                content_type_field_name='content_type',
                parent_field=MenuItem._meta.get_field('content_type'),
            )
        }