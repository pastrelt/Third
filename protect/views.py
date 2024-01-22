from django.shortcuts import render
from articles.models import Category, Categories_subscribers

# Добавляем проверку аутентификации.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SubscribeForm

# Настройки Celery.
# Базовой структурной единицей системы Celery является task (задача).
from django.http import HttpResponse
from django.views import View

# Пример из учебника.
#from .tasks import hello


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        # Передаем информацию о катеориях для возможности подписки.
        context['categories'] = Category.objects.all()
        context['form'] = SubscribeForm()
        return context

    # Сохранение выбранных категорий для пользователя.
    def post(self, request, *args, **kwargs):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            selected_category = form.cleaned_data['categories']
            for category in selected_category:
                category_id = Category.objects.get(pk=category.id)
                categories_subscribers, created = (Categories_subscribers.objects.get_or_create(
                                                                user=request.user,
                                                                category_id=category_id.id))

        return super().get(request, *args, **kwargs)

    # Пример из учебника.
    # Напишем простую задачу, которая будет выводить «Hello, world!» в консоль.
    # Демонстрация работы Celery!
    # def get(self, request):
    #     hello.delay()
    #     return HttpResponse('Hello!')
