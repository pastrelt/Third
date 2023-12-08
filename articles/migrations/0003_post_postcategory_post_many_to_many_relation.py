# Generated by Django 4.2.6 on 2023-12-06 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_or_news', models.CharField(choices=[('статья', 'статья'), ('новость', 'новость')], max_length=7)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('text_article_or_news', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='many_to_many_relation',
            field=models.ManyToManyField(through='articles.PostCategory', to='articles.category'),
        ),
    ]
