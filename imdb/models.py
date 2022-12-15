from django.db import models
from django.core.validators import MinValueValidator


class Movie(models.Model):
    image = models.SlugField(max_length=100)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    weekend = models.DecimalField(max_digits=6, decimal_places=2)
    gross = models.DecimalField(max_digits=6, decimal_places=2)
    weeks = models.CharField(max_length=3)

    def __str__(self):
        return self.title