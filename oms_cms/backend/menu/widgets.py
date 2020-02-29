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

import json

from random import randint

from django.urls import reverse, NoReverseMatch
import django.forms


class GfkLookupWidget(django.forms.Widget):
    """This widget provides a link next to a text field for selecting objects
    related by GenericForeignKeys.
    It's a wad of JavaScript that inspects the select box generated for the
    contenttypes framework's content_type field and uses Django's normal
    showRelatedObjectLookupPopup to populate the text field represented by this
    widget.
    This widget is compatible with inlines.
    """

    def __init__(self, *args, **kwargs):
        """Args:
            content_type_field_name: This is name of the field that becomes a
                select box in the admin.
            parent_field: This is a field on the model. It's used to find the
                related content_type field to generate URLs for the choices.
        """
        self.ct_field_name = kwargs.pop('content_type_field_name')
        self.parent_field = kwargs.pop('parent_field')

        super(GfkLookupWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        model = self.parent_field.model
        ct_field = self.parent_field.model._meta.get_field(self.ct_field_name)
        choices = ct_field.get_choices()

        # We'll generate the URLs for each supported content type upfront and
        # store them in a dict indexed on the model name. This will allow the
        # JavaScript to get the URL based on the <select> box markup.
        urls = {}
        for type_id, type_name in choices:
            # This is the default "-------" entry.
            if not type_id:
                continue

            content_type = django.contrib.contenttypes.models\
                .ContentType.objects.get_for_id(type_id)

            # The URLs for the anchors used by showRelatedObjectLookupPopup
            # have the form of:
            #
            #     /<app_label>/<model>/?t=<pk_field_name>
            #     /myapp/foomodel/?t=id
            try:
                url = reverse(
                    'admin:{app}_{model}_changelist'.format(
                        app=content_type.app_label,
                        model=content_type.model))
            except NoReverseMatch:
                # This content type isn't available in the admin, so we can't
                # provide the lookup. This is common, so we'll just ignore this
                # one.
                continue

            urls[type_name] = url

        # When default value is None, input box should be empty.
        if value is None:
            value = ""

        # JavaScript braces need to be doubled due to the string formatting.
        #
        # vForeignKeyRawIdAdminField is required by the popup to target this
        # field.
        #
        # This script must be called from the onclick attribute. When this
        # widget is displayed inline, the DOM nodes are copied from templated
        # nodes and a '__prefix__' token is replaced with the index of the new
        # row. The Django code that does this doesn't do that replacement
        # inside the script node so the IDs end up as
        # 'lookup_id_foomodel_set-__prefix__-foofield'.
        #
        # In this situation the script will have been rendered with a
        # ct_field_name with the __prefix__ template, so  we also need to use
        # the ID on the link node as a template for finding the related select
        # box.
        return django.utils.safestring.mark_safe("""
            <input class="vForeignKeyRawIdAdminField" id="id_{name}" name="{name}" value="{value}" type="text" />
            <a id="lookup_id_{name}" class="related-lookup gfklookup" onclick="return gfklookupwidget_{uniq}_click(django.jQuery, this, event);"></a>
            <script type="text/javascript">
                if (typeof(gfklookupwidget_{uniq}_click) == 'undefined') {{
                    function gfklookupwidget_{uniq}_click($, element, event) {{
                        if (event) {{
                            event.preventDefault();
                        }}
                        var urls = {urls};
                        var $this = $(element);
                        var ct_field_name = "{ct_field_name}";
                        var prefix = "";
                        var id = $this.attr('id');
                        if (id.indexOf('-')) {{
                            ct_field_name = id.substring(0, id.lastIndexOf('-') + 1).replace('lookup_id_', '') + ct_field_name;
                        }}
                        var selected = $('select[name="'+ct_field_name+'"]').find('option:selected');
                        var content_type_id = selected.val();
                        var content_type = selected.text();
                        if (!content_type) {{
                            alert('No content type found for GenericForeignKey lookup.');
                            return false;
                        }}
                        if (!content_type_id) {{
                            alert('You must select: '+ct_field_name+'.');
                            return false;
                        }}
                        $this.attr('href', urls[content_type]);
                        return showRelatedObjectLookupPopup(element);
                    }}
                }}
            </script>
        """.format(
            uniq='{:X}'.format(randint(1, 1000000)),
            name=name,
            value=value,
            urls=json.dumps(urls),
            ct_field_name=self.ct_field_name,
        ))