# Импортируем классы, которые говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .forms import PostForm, ArticleForm
from .filters import PostFilter

# Добавляем для проверки прав доступа.
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin

# Представление прав (добавления - add и изменения - change) дступа приложения articles модели Post.
class MyView(PermissionRequiredMixin, View):
    permission_required = ('articles.add_post',
                           'articles.change_post',)

class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    # Новости выводиться в порядке от более свежей к самой старой.
    ordering = '-date_and_time'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 10  # вот так мы можем указать количество записей на странице

    # Переопределяем функцию получения списка статей.
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список статей
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class ArticleDetail(DetailView):
       # Модель всё та же, но мы хотим получать информацию по отдельной статье.
       model = Post
       # Используем другой шаблон — article.html
       template_name = 'article.html'
       # Название объекта, в котором будет выбранная пользователем статья.
       context_object_name = 'article'

# Добавляем новое представление для создания Новостей.
class NewsCreate(CreateView):
    # Проверка доступа на добавление.
    permission_required = ('articles.add_post',)

    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'

# Добавляем представление для изменения Новостей.
class NewsUpdate(UpdateView):
    # Проверка доступа на изменение.
    permission_required = ('articles.change_post',)

    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

# Представление удаляющее Новости.
class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


# Добавляем новое представление для создания Статей.
class ArticleCreate(CreateView):
    # Проверка доступа на добавление.
    permission_required = ('articles.add_post',)

    form_class = ArticleForm
    model = Post
    template_name = 'articl_edit.html'

# Добавляем представление для изменения Статей.
class ArticleUpdate(UpdateView):
    # Проверка доступа на изменение.
    permission_required = ('articles.change_post',)

    form_class = ArticleForm
    model = Post
    template_name = 'articl_edit.html'

# Представление удаляющее Статьи.
class ArticleDelete(DeleteView):
    model = Post
    template_name = 'articl_delete.html'
    success_url = reverse_lazy('news_list')