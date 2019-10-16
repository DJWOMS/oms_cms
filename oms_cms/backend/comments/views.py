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
    # def post(self, request, *args, **kwargs):
    #     form = CommentsForm(request.POST)
    #     if form.is_valid():
    #         form = form.save(commit=False)
    #         form.user = request.user
    #         form.post = Post.objects.get(comments=self.kwargs.get('pk'))
    #         comm_1 = self.model.objects.get(id=self.kwargs.get('pk'))
    #         form.text = comm_1.user.username + ', ' + form.text
    #         form.save()
    #         form.move_to(comm_1)
    #         return redirect('new-detail',
    #                         lang=self.kwargs.get('lang'),
    #                         category=self.kwargs.get('category'),
    #                         post=self.kwargs.get('post'))
#
#
# class DeleteComment(View):
#     """Удаление комментария"""
#     def post(self, request, pk):
#         comm = get_object_or_404(Comments, id=pk, user=request.user)
#         comm.delete()
#         return redirect('new-detail', lang=lang, category=category, post=post)


from django import http
from django.apps import apps
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import escape
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

import django_comments
from django_comments import signals
from django_comments.views.utils import next_redirect, confirmation_view


class CommentPostBadRequest(http.HttpResponseBadRequest):
    """
    Response returned when a comment post is invalid. If ``DEBUG`` is on a
    nice-ish error message will be displayed (for debugging purposes), but in
    production mode a simple opaque 400 page will be displayed.
    """

    def __init__(self, why):
        super(CommentPostBadRequest, self).__init__()
        if settings.DEBUG:
            self.content = render_to_string("comments/400-debug.html", {"why": why})


@csrf_protect
@require_POST
def post_comment(request, next=None, using=None):
    """
    Post a comment.

    HTTP POST is required. If ``POST['submit'] == "preview"`` or if there are
    errors a preview template, ``comments/preview.html``, will be rendered.
    """
    # Fill out some initial data fields from an authenticated user, if present
    data = request.POST.copy()
    if request.user.is_authenticated:
        if not data.get('name', ''):
            data["name"] = request.user.get_full_name() or request.user.get_username()
        if not data.get('email', ''):
            data["email"] = request.user.email

    # Look up the object we're trying to comment about
    ctype = data.get("content_type")
    object_pk = data.get("object_pk")
    if ctype is None or object_pk is None:
        return CommentPostBadRequest("Missing content_type or object_pk field.")
    try:
        model = apps.get_model(*ctype.split(".", 1))
        target = model._default_manager.using(using).get(pk=object_pk)
    except TypeError:
        return CommentPostBadRequest(
            "Invalid content_type value: %r" % escape(ctype))
    except AttributeError:
        return CommentPostBadRequest(
            "The given content-type %r does not resolve to a valid model." % escape(ctype))
    except ObjectDoesNotExist:
        return CommentPostBadRequest(
            "No object matching content-type %r and object PK %r exists." % (
                escape(ctype), escape(object_pk)))
    except (ValueError, ValidationError) as e:
        return CommentPostBadRequest(
            "Attempting go get content-type %r and object PK %r exists raised %s" % (
                escape(ctype), escape(object_pk), e.__class__.__name__))

    # Do we want to preview the comment?
    preview = "preview" in data

    # Construct the comment form
    form = django_comments.get_form()(target, data=data)

    # Check security information
    if form.security_errors():
        return CommentPostBadRequest(
            "The comment form failed security verification: %s" % escape(str(form.security_errors())))

    # If there are errors or if we requested a preview show the comment
    if form.errors or preview:
        template_list = [
            # These first two exist for purely historical reasons.
            # Django v1.0 and v1.1 allowed the underscore format for
            # preview templates, so we have to preserve that format.
            "comments/%s_%s_preview.html" % (model._meta.app_label, model._meta.model_name),
            "comments/%s_preview.html" % model._meta.app_label,
            # Now the usual directory based template hierarchy.
            "comments/%s/%s/preview.html" % (model._meta.app_label, model._meta.model_name),
            "comments/%s/preview.html" % model._meta.app_label,
            "comments/preview.html",
        ]
        return render(request, template_list, {
                "comment": form.data.get("comment", ""),
                "form": form,
                "next": data.get("next", next),
            },
        )

    # Otherwise create the comment
    comment = form.get_comment_object(site_id=get_current_site(request).id)
    comment.ip_address = request.META.get("REMOTE_ADDR", None) or None
    if request.user.is_authenticated:
        comment.user = request.user
        # if data.get("comment_perent", None) is not None:
        #     comm_1 = django_comments.get_model().get(id=data.get("comment_perent"))
        #     comment.comment = comm_1.user.username + ', ' + comment.comment
        #     form.move_to(comm_1)
    # Signal that the comment is about to be saved
    responses = signals.comment_will_be_posted.send(
        sender=comment.__class__,
        comment=comment,
        request=request
    )

    for (receiver, response) in responses:
        if response is False:
            return CommentPostBadRequest(
                "comment_will_be_posted receiver %r killed the comment" % receiver.__name__)

    # Save the comment and signal that it was saved
    comment.save()
    if data.get("comment_parent", None) is not None and data.get("comment_parent") != '':
        comm_1 = django_comments.get_model().objects.get(id=data.get("comment_parent"))
        # comment.comment = comm_1.user.username + ', ' + comment.comment
        comment.move_to(comm_1)
    signals.comment_was_posted.send(
        sender=comment.__class__,
        comment=comment,
        request=request
    )

    return next_redirect(request, fallback=next or 'comments-comment-done',
                         c=comment._get_pk_val())


comment_done = confirmation_view(
    template="comments/posted.html",
    doc="""Display a "comment was posted" success page."""
)
