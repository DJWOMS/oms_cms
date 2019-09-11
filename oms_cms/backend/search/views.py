from django.db.models import Q
from django.views.generic import ListView
from django.conf import settings
from django.apps import apps

from .models import SpySearch


class SearchView(ListView):
    """Поиск на сайте"""
    paginate_by = settings.SEARCH_PAGINATE
    template_name = settings.SEARCH_TEMPLATE
    context_object_name = "search_list"
    question = None
    models = None

    def get_queryset(self):
        search_results = []
        if self.get_search_form():
            for item in settings.SEARCH_MODELS:
                app, model, *fields = item
                if model in self.models:
                    model = apps.get_model(app, model)
                    #[x for x in model._meta.fields] # if isinstance(x, django.db.models.CharField)]
                    search_queries = [Q(**{x + "__icontains": self.question}) for x in fields] #__unaccent
                    q_object = Q()
                    for query in search_queries:
                        q_object = q_object | query

                    results = model.objects.filter(q_object)
                    search_results.append(results)

        return search_results

    def get_search_form(self):
        """Проверка данных поиска"""
        self.question = self.request.GET.get('q', None)
        models = self.request.GET.getlist('models[]')
        if self.question is not None:
            if models:
                self.models = models
            else:
                self.models = [i[1] for i in settings.SEARCH_MODELS]
            self.save_question()
            return True
        else:
            return False

    def save_question(self):
        """Сохранение запроса"""
        rec, a = SpySearch.objects.get_or_create(record=self.question)
        rec.counter += 1
        rec.save()
