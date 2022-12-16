from django.db import models
from django.core.validators import MinValueValidator


class Movie(models.Model):
    image = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    weekend = models.CharField(max_length=10)
    gross = models.CharField(max_length=10)
    weeks = models.CharField(max_length=3)

    def __str__(self):
        return self.title