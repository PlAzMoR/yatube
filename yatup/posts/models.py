from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, db_index=True, verbose_name='URL', unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, related_name='post', verbose_name='Автор', on_delete=models.CASCADE)

    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text

