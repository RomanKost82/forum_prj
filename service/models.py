from enum import auto
from tabnanny import verbose
from turtle import title
from django.db import models
from django.urls import reverse, reverse_lazy


class Post(models.Model):

    title = models.CharField(verbose_name='название', max_length=250)
    desc = models.TextField(verbose_name='описание', null=True, blank=True)
    image = models.ImageField(verbose_name='картинка', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('index')


class Comment(models.Model):
    desc = models.TextField(verbose_name='описание', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.desc}'

    def get_absolute_url(self):
        return reverse_lazy('index')
