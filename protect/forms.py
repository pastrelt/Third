from django import forms
from django.core.exceptions import ValidationError
from articles.models import Category

# Форма выбора Category для подписки после регистрации.
class SubscribeForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        )