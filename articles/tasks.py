""" Проверка док. сторки"""
# Базовой структурной единицей системы Celery является task (задача).
# Все задачи принято хранить в файлах с названием tasks.py.
from celery import shared_task
import time

# Добавляем для задачи send_weekly_articles - еженедельная рассылка с последними новостями за неделю.
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import Categories_subscribers
from .models import Category
from .models import Post
from django.core.mail import send_mail


# Задача хорошо помоает проверить работу серверов Celery.
# @shared_task
# def printer(N):
#     for i in range(N):
#         time.sleep(1)
#         print(i+1)


# Задача - рассылка уведомлений подписчикам после создания новости.
@shared_task
def sending_notifications(category, user_email, html_content):
    send_mail(
        subject=f'Рассылка уведомлений подписчикам категории {category}, после создания новости.',  # тема письма обязательный параметр
        message="",  # обязательный параметр
        from_email='passtreltsov@yandex.ru',  # здесь указываю почту, с которой буду отправлять
        recipient_list=[user_email],  # здесь список получателей.
        html_message=html_content  # Добавляем свёрстанный HTML-шаблон
    )


# Задача - еженедельная рассылка с последними новостями за неделю.
@shared_task
def send_weekly_articles():

    # Получаем текущую дату и время
    current_date = timezone.now()

    # Определяем начальную и конечную даты для выборки статей за неделю
    start_date = current_date - timedelta(days=7)
    end_date = current_date

    # Получаем все категории
    categories = Category.objects.all()
    for category_name in categories:

        # Получаем подписчиков категории
        subscribers = category_name.subscribers.all()

        # Получаем новые статьи для данной категории за последнюю неделю
        new_articles = Post.objects.filter(
            category=category_name,
            date_and_time__range=(start_date, end_date)
        )

        # Формируем список новых статей с гиперссылками на них
        article_list = "\n".join([f"{article.title}: http://127.0.0.1:8000{article.get_absolute_url()}"
                                  for article in new_articles])

        # Отправляем письмо со списком новых статей подписчикам категории
        for subscriber in subscribers:
            send_mail(
                f"Новые статьи в категории '{category_name}' за последнюю неделю",
                article_list,
                "passtreltsov@yandex.ru",
                [subscriber.email] # FIXME # TODO
            )