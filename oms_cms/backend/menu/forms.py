from django.contrib.admin import site
from django.forms import ModelForm
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.db.models.fields.related import ManyToOneRel
from .widgets import ContentTypeSelect
from .models import MenuItem
from oms_cms.backend.pages.models import Pages


class AdminRatingForm(ModelForm):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # try:
            model = self.instance.content_type.model_class()
            #     model_key = model._meta.get_field('id').rel
            # except:
            #     model = Pages
            #     model_key = 'id'
            self.fields['object_id'].widget = ForeignKeyRawIdWidget(model._meta.get_field('id').remote_field, site)
            # self.fields['object_id'].widget = ForeignKeyRawIdWidget(model_key, site)
            # self.fields['object_id'].widget = ForeignKeyRawIdWidget(ManyToOneRel(model, model_key), site),
            # self.fields['content_type'].widget.widget = ContentTypeSelect('lookup_id_object_id',
            #                 self.fields['content_type'].widget.widget.attrs,
            #                 self.fields['content_type'].widget.widget.choices)

    class Meta:
        model = MenuItem
        fields = ['title', 'menu', 'name', 'content_type', 'parent', 'object_id']
        widgets = {
            # "object_id": ForeignKeyRawIdWidget(imodel._meta.get_field('customer').remote_field, site),
            # "content_type":  ContentTypeSelect('lookup_id_object_id',
            #                 fields['content_type'].attrs,
            #                 fields['content_type'].choices)
        }