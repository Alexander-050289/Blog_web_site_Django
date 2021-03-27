import datetime
from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('article_name', max_length=200)
    article_text = models.TextField('text')
    pub_date = models.DateTimeField('date')

    def __str__(self):
        return self.article_title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('author_name', max_length=50)
    comment_text = models.CharField('comment_text', max_length=200)

    def __str__(self):
        return self.author
