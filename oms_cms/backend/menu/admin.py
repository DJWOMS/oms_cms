from django.contrib import admin
from django import forms
from mptt.admin import MPTTModelAdmin
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline, GenericInlineModelAdmin
from .models import Menu, MenuItem
from .forms import AdminRatingForm


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # maybe you can find better solution to get app_label
        return "{}".format(obj)


# class FieldForm(forms.ModelForm):
#     content_type = CustomModelChoiceField(queryset=ContentType.objects.all())
#     #object_id = forms.IntegerField(widget=forms.ChoiceField(choices=((1, "content_type"),)))
#     class Meta:
#         model = MenuItem
#         fields = ('object_id',)
#         widgets = {
#             'object_id': forms.Select(choices=(content_type))
#         }


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Меню"""
    list_display = ("name", "status")


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Пункты меню"""
    # form = FieldForm
    list_display = ("title", "name", "parent", "lang", "menu", "id")
    mptt_level_indent = 20
    list_filter = ("menu", "parent", "lang")
    search_fields = ("name", "parent", "menu")
    # form = AdminRatingForm
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'name',
    #             'title',
    #             'parent',
    #             'menu',
    #             "status",
    #         ),
    #
    #     }),
    #     ('Ссылки', {
    #         'fields': (
    #             'url',
    #             'anchor',
    #             'content_type',
    #             'object_id'
    #         )
    #     }),
    # )
    # raw_id_fields = ('related_fk', 'related_m2m',)
    # define the autocomplete_lookup_fields
    # autocomplete_fields = ['content_type', 'object_id']
    # autocomplete_fields = (
    #     'content_type',
    # )


    # for c in ContentType.objects.all():
    #     print(c.app_label, c.model)



# admin.site.register(MenuItem, MenuItemAdmin)
