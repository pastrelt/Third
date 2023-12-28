from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsCreate, NewsUpdate, NewsDelete
from .views import ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко постам у нас останется пустым.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', NewsList.as_view(), name='news_list'),
    # pk — это первичный ключ поста, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', ArticleDetail.as_view(), name='article_detail'),

    # Работа со страничками новостей.
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),

    # Работа со страничками статей.
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),

]
