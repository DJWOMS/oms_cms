# from django import forms
# from django_comments.forms import CommentForm
# from oms_cms.backend.comments.models import OmsComment
#
#
# class OMSCommentForm(CommentForm):
#     title = forms.CharField(max_length=300)
#
#     def get_comment_create_data(self):
#         data = super(OMSCommentForm, self).get_comment_create_data()
#         data['title'] = self.cleaned_data['title']
#         return data