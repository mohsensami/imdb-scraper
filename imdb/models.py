from django.db import models


class Movie(models.Model):
    tite = models.CharField(max_length=200)