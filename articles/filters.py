#import django_filters
from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter
from django.contrib.auth.models import User
from django import forms
from .models import Post


class DateInput(forms.DateInput):
    input_type = 'date'

# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
class PostFilter(FilterSet):
    # Фильтруем по названию.
    # Meta не может изменить названия полей поиска.
    title = CharFilter(lookup_expr='startswith',
                       label='Заголовок')
    # Фильтруем по имени автора.
    # Meta не может выводить поля не из указанной модели.
    # Исползуем ModelMultipleChoiceFilter для реализации выбора из списка.
    author_username = ModelMultipleChoiceFilter(field_name='author__author__username',
                                        queryset=User.objects.all(),
                                        #empty_label='Не выбран',
                                        lookup_expr='exact',
                                        label='Автор',
                                        conjoined=False) # False - более наглядно.
    # Фильтруем позже указываемой даты.
    # Meta не может добавить виджет.
    date_and_time__gt = CharFilter(field_name='date_and_time',
                                   widget=DateInput,
                                   lookup_expr='gt',
                                   label='Дата')
    # Meta не нужен.
    # class Meta:
    #     # В Meta классе мы должны указать Django модель,
    #     # в которой будем фильтровать записи.
    #     model = Post
    #     # В fields мы описываем по каким полям модели
    #     # будет производиться фильтрация.
    #     fields = { 'title' }
