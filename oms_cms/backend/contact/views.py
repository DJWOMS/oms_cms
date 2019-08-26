from django.conf import settings
from django.contrib import messages
from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import CreateView, View

from .models import Feedback
from .forms import FeedbackFullForm


class FeedbackView(CreateView):
    """Форма обратной связи"""
    model = Feedback
    form_class = FeedbackFullForm
    template_name = 'contact/feedback.html'

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, settings.MESSAGE_LEVEL, "Ваше сообщение отправленно")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, settings.MESSAGE_LEVEL, "Ошибка")
        return super().form_valid(form)


class FeedbackFormView(View):
    """Обработка сгенирированной формы обратной связи"""
    def post(self, request):
        value = request.POST.get("honeypot")
        if value:
            raise Http404
        fields = FeedbackFullForm().fields
        result_fields = list(set(fields) & set(request.POST.keys()))
        gen_form = modelform_factory(Feedback, fields=(result_fields))
        form = gen_form(request.POST)
        # form = self._get_form(request, gen_form, 'aform_pre')
        if form.is_valid():
            form.save()
        return redirect(request.POST.get("next", "/"))

    # def _get_form(self, request, formcls, prefix):
    #     data = request.POST if prefix in request.POST else None
    #     return formcls(data, prefix=prefix)