from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from .models import Post, Author


class PostForm(forms.ModelForm):
    #queryset_user = User.objects.all()

    # Первичные устаноки отдельных полей.
    article_or_news = forms.CharField(initial="новость", widget=forms.HiddenInput()) # не выводим на экран.
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

class ArticleForm(forms.ModelForm):
    #queryset_user = User.objects.all()

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