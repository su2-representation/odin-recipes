from django.db import models
from django.contrib.postgres.fields import ArrayField


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = ArrayField(models.TextField(), default=list)
    ingredients = ArrayField(models.CharField(max_length=150), default=list)
    steps = ArrayField(models.TextField(), default=list)
    img = models.CharField(max_length=300)

    def __str__(self):
        return self.title
