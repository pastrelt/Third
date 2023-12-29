from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Здесь мы импортировали класс формы, который предоставляет allauth, а также модель групп.
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )


# Ппереопределить класс формы так,
# чтобы при успешном прохождении регистрации добавлять присоединение к базовой группе пользователей.
# В первой строке метода мы вызываем этот же метод класса-родителя,
# чтобы необходимые проверки и сохранение в модель User были выполнены.
# Далее мы получаем объект модели группы basic. И в следующей строке, через атрибут user_set,
# возвращающий список всех пользователей этой группы, мы добавляем нового пользователя в эту группу.
# Обязательным требованием метода save() является возвращение объекта модели User по итогу выполнения функции.
class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user