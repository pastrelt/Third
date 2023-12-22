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
    author = forms.ModelChoiceField(queryset=User.objects.all(),
                                    label='Автор',
                                    widget=forms.Select,
                                    initial=User.objects.first(),
                                    to_field_name='username')

    # def save(self, commit=True):
    #     instance = super(PostForm, self).save(commit=False)
    #     author_instance, created = Author.objects.get_or_create(user=instance.author)
    #     instance.author = author_instance
    #     if commit:
    #         instance.save()
    #     return instance

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
    author = forms.ModelChoiceField(queryset=User.objects.all(),
                                    label='Автор',
                                    widget=forms.Select,
                                    initial=User.objects.first(),
                                    to_field_name='username')

    # def save(self, commit=True):
    #     instance = super(PostForm, self).save(commit=False)
    #     author_instance, created = Author.objects.get_or_create(user=instance.author)
    #     instance.author = author_instance
    #     if commit:
    #         instance.save()
    #     return instance

    class Meta:
        model = Post
        fields = [
            'article_or_news',
            'title',
            'text_article_or_news',
            'author',
        ]