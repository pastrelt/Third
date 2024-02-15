from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

# Импортировал модель групп, и декоратор проверки аутентификации.
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Логирование.
import logging

logger = logging.getLogger('django.security')


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

# Ддобавил ещё одно view для апгрейда аккаунта до Authors.
# В этом листинге кода мы получили объект текущего пользователя из переменной запроса.
# Вытащили authors-группу из модели Group. Дальше мы проверяем,
# находится ли пользователь в этой группе (вдруг кто-то решил перейти по этому URL, уже имея Authors).
# И если он всё-таки ещё не в ней — смело добавляем.
@login_required
def upgrade_me(request):
    user = request.user

    # Лоирование имени пользователя.
    logger.info(f'Пользователь: {user}')

    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')