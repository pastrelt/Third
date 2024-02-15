"""
URL configuration for News_Portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Делаем так, чтобы все адреса из нашего приложения (articles/urls.py)
    # подключались к главному приложению с префиксом news/.
    path('news/', include('articles.urls')),

    # Добавил перенаправление корневой страницы в приложение protect.
    path('', include('protect.urls')),

    # Все страницы, URL которых начинается с sign/, перенаправляю в приложение sign.
    path('sign/', include('sign.urls')),

    # Добавил перенаправление на ‘accounts/’ для всех URL, которые будут управляться подключенным пакетом.
    path('accounts/', include('allauth.urls')),

    # Все страницы, URL которых начинается с articles/, перенаправляю в приложение articles/urls_articles.py .
    # исправление ошибки предыдущео задания.
    path('article/', include('articles.urls_articles')),
]
