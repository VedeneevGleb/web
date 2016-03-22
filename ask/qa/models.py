from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField()
    text = models.CharField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)


class Answer(models.Model):
    text = models.CharField()
    added_at = models.DateField()
    question = models.OneToOneField(Question)
    author = models.ForeignKey(User)
