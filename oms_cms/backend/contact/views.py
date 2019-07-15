from django.conf import settings
from django.contrib import messages
from django.views.generic import CreateView

from .models import Feedback
from .forms import FeedbackForm


class FeedbackView(CreateView):
    """Форма обратной связи"""
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact/feedback.html'

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, settings.MESSAGE_LEVEL, "Ваше сообщение отправленно")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, settings.MESSAGE_LEVEL, "Ошибка")
        return super().form_valid(form)
