from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title