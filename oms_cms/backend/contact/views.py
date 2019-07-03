from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.base import View

from .models import Feedback
from .forms import FeedbackForm


class AddFeedback(View):
    """Добавление сообщения обратной связи"""
    def post(self, request):
        full_name = request.POST.get("full_name")
        tel = request.POST.get("tel")
        email = request.POST.get("email")

        if tel and full_name:
            Feedback.objects.create(tel=tel, full_name=full_name)
        elif email:
            Feedback.objects.create(email=email)
        else:
            return HttpResponse("Ошибка отправки", status=400)

        # return redirect('/')
        return HttpResponse("Заявка принята", status=201)


class FeedbackView(CreateView):
    """Добавление сообщения обратной связи"""
    template_name = "contact/add_feedbac.html"
    model = Feedback
    form_class = FeedbackForm
