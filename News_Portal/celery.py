import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News_Portal.settings')

app = Celery('News_Portal')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# Расписание, по которому должны будут запускаться задачи.
# Само расписание представляет собой словарь словарей.
# Ключ основного словаря — это имя периодической задачи.
# Значение — это словарь с параметрами периодической задачи — сама задача, которая будет выполняться, аргументы,
# а также параметры расписания.
# Это периодическое задание хорошо помоает проверить работу серверов Celery.
# app.conf.beat_schedule = {
#     'print_every_5_seconds': {
#         'task': 'articles.tasks.printer',
#         'schedule': 5,
#         'args': (5,),
#     },
# }


app.conf.beat_schedule = {
    'weekly_newsletter_every_мonday_8_am': {
        'task': 'articles.tasks.send_weekly_articles',
        # проверка crontab()
        # 'schedule': crontab(),
        # работает!
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': (),
    },
}