from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


## 1. Модель Author
# Модель, содержащая объекты всех авторов.
# Имеет следующие поля:
# cвязь «один к одному» с встроенной моделью пользователей User;
# рейтинг пользователя. Ниже будет дано описание того, как этот рейтинг можно посчитать.
class Author(models.Model):  # наследуемся от класса Model
    author = models.OneToOneField(User, on_delete = models.CASCADE)
    author_rating = models.IntegerField(default = 0)

    # 2.3 Метод update_rating() модели Author, который обновляет рейтинг текущего автора
    # (метод принимает в качестве аргумента только self).
    def update_rating(self):
        # Суммарный рейтинг каждой статьи автора умножается на 3;
        articles_rating = 0
        articles = Post.objects.filter(author=self)
        for article in articles:
            articles_rating += article.rating * 3

        # Суммарный рейтинг всех комментариев автора;
        comments_rating = 0
        comments = Comment.objects.filter(post__author=self)
        for comment in comments:
            comments_rating += comment.rating

        # Суммарный рейтинг всех комментариев к статьям автора.
        comments_to_articles_rating = 0
        for article in articles:
            article_comments = Comment.objects.filter(post=article)
            for comment in article_comments:
                comments_to_articles_rating += comment.rating

        self.author_rating = articles_rating + comments_rating + comments_to_articles_rating
        self.save()


# 2. Модель Category
# Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.).
# Имеет единственное поле: название категории. Поле должно быть уникальным
# (в определении поля необходимо написать параметр unique = True).
class Category(models.Model):
    name_of_category = models.CharField(max_length=100, unique=True)



# 3. Модель Post
# Эта модель должна содержать в себе статьи и новости, которые создают пользователи.
# Каждый объект может иметь одну или несколько категорий.
# Соответственно, модель должна включать следующие поля:
# связь «один ко многим» с моделью Author;
# поле с выбором — «статья» или «новость»;
# автоматически добавляемая дата и время создания;
# связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
# заголовок статьи/новости;
# текст статьи/новости;
# рейтинг статьи/новости.
class Post(models.Model):
    author = models.ForeignKey('Author', on_delete = models.CASCADE)
    article_or_news = models.CharField(max_length=7, choices=[('статья', 'статья'), ('новость', 'новость')])
    date_and_time = models.DateTimeField(auto_now_add = True)
    many_to_many_relation = models.ManyToManyField('Category', through = 'PostCategory')
    title =  models.CharField(max_length = 255)
    text_article_or_news = models.TextField()
    rating = models.IntegerField(default = 0)

    # Методы like() и dislike() увеличивают/уменьшают рейтинг на единицу.
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    #  Превью статьи. Возвращает начало статьи (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
    def preview(self):
        preview = self.text_article_or_news[:124] + '...'
        return preview

    # Форматирование вывода данных для вывода на основную страницу.
    def __str__(self):
        return (f'{self.title.title()}   '
                f'{self.date_and_time.strftime('%d-%m-%Y %H:%M:%S')}   '
                f'{self.text_article_or_news[:20]}')

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


# 4. Модель PostCategory
# Промежуточная модель для связи «многие ко многим»:
# связь «один ко многим» с моделью Post;
# связь «один ко многим» с моделью Category.
class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)


# 5. Модель Comment
# Под каждой новостью/статьёй можно оставлять комментарии,
# поэтому необходимо организовать их способ хранения тоже.
# Модель будет иметь следующие поля:
# связь «один ко многим» с моделью Post;
# связь «один ко многим» со встроенной моделью User
# (комментарии может оставить любой пользователь, необязательно автор);
# текст комментария;
# дата и время создания комментария;
# рейтинг комментария.
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text_comment = models.TextField()
    date_and_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    # Методы like() и dislike() увеличивают/уменьшают рейтинг на единицу.
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
