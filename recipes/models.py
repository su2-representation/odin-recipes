from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    img = models.CharField(max_length=300)

    def __str__(self):
        return self.title
