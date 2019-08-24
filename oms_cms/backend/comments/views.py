from urllib.parse import urlencode

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.utils.http import is_safe_url
from django.views import View
from django.forms import modelform_factory
from django.views.generic import UpdateView

from oms_cms.backend.comments.models import OmsComment
# from oms_cms.backend.comments.forms import CommentsForm, EditCommentsForm
#
#
# class AddCommentMixin:
#     """Добавление комментария"""
#     def create_comment(self, model):
#         fields = CommentsForm().fields
#         result_fields = list(set(fields) & set(self.request.POST.keys()))
#         gen_form = modelform_factory(Comments, fields=(result_fields))
#         form = gen_form(self.request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             if self.request.user.is_authenticated:
#                 form.user = self.request.user
#             form.content_object = model
#             form.save()
#             return True
#         else:
#             return False

    # def next_url(self):
    #     next = self.request.POST.get('next')
    #     if not is_safe_url(url=next, allowed_hosts={self.request.get_host()}):
    #         next = resolve_url(fallback)
    #
    #     if get_kwargs:
    #         if '#' in next:
    #             tmp = next.rsplit('#', 1)
    #             next = tmp[0]
    #             anchor = '#' + tmp[1]
    #         else:
    #             anchor = ''
    #
    #         joiner = ('?' in next) and '&' or '?'
    #         next += joiner + urlencode(get_kwargs) + anchor
    #     return HttpResponseRedirect(self.get_success_url())


# class CreateCommentView(AddCommentMixin, View):
#     """Добавление комментария"""
#
#     def post(self, request, **kwargs):
#         self.create_comment(Post.objects.get(slug=kwargs.get("post")))
#         return self.next_url()
#
#
# class EditCommentView(View):
#     """Редактирование комментария"""
#     model = None
#     template_name = 'comments/comment_create.html'
#     success_url = None
#
#     def get(self, request, **kwargs):
#         comment = get_object_or_404(Comments, id=kwargs.get("pk"), user=request.user)
#         form = EditCommentsForm(instance=comment)
#         return render(request, self.template_name, {"comment_form": form})
#
#     def post(self, request, **kwargs):
#         comment = get_object_or_404(Comments, id=kwargs.get("pk"), user=request.user)
#         form = EditCommentsForm(instance=comment, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return self.form_valid()
#         else:
#             return self.form_invalid()
#
#     def get_success_url(self):
#         if not self.success_url and self.model:
#             self.success_url = self.model.objects.get(comments__id=self.kwargs.get("pk")).get_absolute_url()
#         elif not self.success_url and not self.model:
#             raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
#         return str(self.success_url)
#
#     def form_valid(self):
#         pass
#
#     def form_invalid(self):
#         return HttpResponseRedirect(self.get_success_url())


# class EditComment(UpdateView):
#     """Редактирование комментария"""
#     model = Comments
#     form_class = EditCommentsForm
#     template_name = 'comments/comment_create.html'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         self.success_url = Post.objects.get(comments=self.object.id).get_absolute_url()
#         form.save()
#         return super(EditComment, self).form_valid(form)


# class AnswerComment(CreateView):
#     """Ответ на комментарий"""
#     model = Comments
#     form_class = CommentsForm
#     template_name = 'news/comment_create.html'
#
#     def post(self, request, *args, **kwargs):
#         form = CommentsForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user = request.user
#             form.post = Post.objects.get(comments=self.kwargs.get('pk'))
#             comm_1 = self.model.objects.get(id=self.kwargs.get('pk'))
#             form.text = comm_1.user.username + ', ' + form.text
#             form.save()
#             form.move_to(comm_1)
#             return redirect('new-detail',
#                             lang=self.kwargs.get('lang'),
#                             category=self.kwargs.get('category'),
#                             post=self.kwargs.get('post'))
#
#
# class DeleteComment(View):
#     """Удаление комментария"""
#     def post(self, request, pk):
#         comm = get_object_or_404(Comments, id=pk, user=request.user)
#         comm.delete()
#         return redirect('new-detail', lang=lang, category=category, post=post)

