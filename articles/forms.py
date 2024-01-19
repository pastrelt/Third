from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Author, Category


# Форма для просмотра новостей вход через news/.
class PostForm(forms.ModelForm):
    # Первичные устаноки отдельных полей.
    article_or_news = forms.CharField(initial="новость", widget=forms.HiddenInput()) # не выводим на экран.
    title = forms.CharField(label='Заголовок')
    text_article_or_news = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    author = forms.ModelChoiceField(queryset=Author.objects.all(),
                                    label='Автор',
                                    widget=forms.Select,
                                    initial=Author.objects.first(),
                                    to_field_name='author')
    # Добавляем поле category для отправки сообщения если на категорию есть подписка.
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                    label='Категория',
                                    widget=forms.Select,
                                    initial=Category.objects.first(),
                                    to_field_name='name_of_category')

    class Meta:
        model = Post
        fields = [
            'article_or_news',
            'title',
            'text_article_or_news',
            'category',
            'author',
        ]


# Форма для просмотра статей вход через article/.
class ArticleForm(forms.ModelForm):

    # Первичные устаноки отдельных полей.
    article_or_news = forms.CharField(initial="статья", widget=forms.HiddenInput()) # не выводим на экран.
    title = forms.CharField(label='Заголовок')
    text_article_or_news = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    author = forms.ModelChoiceField(queryset=Author.objects.all(),
                                    label='Автор',
                                    widget=forms.Select,
                                    initial=Author.objects.first(),
                                    to_field_name='author',
                                    )

    class Meta:
        model = Post
        fields = [
            'article_or_news',
            'title',
            'text_article_or_news',
            'author',
        ]