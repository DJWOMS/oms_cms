# Copyright (c) 2013, Mason Staugler
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

import django.db.models
import django.forms
import django.forms.fields

from  oms_cms.backend.menu.widgets import GfkLookupWidget


class GfkLookupField(django.db.models.PositiveIntegerField):
    """This is a subclass of django.db.models.PositiveIntegerField to be used
    as a replacement for the object_id field in generic relations from the
    contenttypes framework.
    It will provide a link next to the field that will popup a search box based
    on the content_type field currently selected by the user.
    """

    def __init__(self, content_type_field_name=None, *args, **kwargs):
        """When you created you generic relation, you added a 'content_type'
        field (a foreign key to the contenttypes framework). The
        content_type_field_name is a string with the name of that field.
        This field is required, but initialized to None so that it will work
        with South migrations.
        """

        self.content_type_field_name = content_type_field_name
        super(GfkLookupField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': GfkLookupFormField,
            # The widget needs to know which select box to inspect for the
            # user's selected content type.
            'content_type_field_name': self.content_type_field_name,
            # The widget needs a reference here so that it can get at the
            # parent Model.
            'parent_field': self,
        }
        defaults.update(kwargs)
        return super(GfkLookupField, self).formfield(**defaults)


class GfkLookupFormField(django.forms.IntegerField):
    """This is a pass-through for the GfkLookupField to define the widget."""

    def __init__(self, content_type_field_name, parent_field, *args, **kwargs):
        kwargs['widget'] = GfkLookupWidget(
            # Pass-through for the GfkLookupField.
            content_type_field_name=content_type_field_name,
            parent_field=parent_field,
        )
        return super(GfkLookupFormField, self).__init__(*args, **kwargs)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^fields\.GfkLookupField"])
except:
    pass