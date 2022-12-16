from django.db import models


class Movie(models.Model):
    CAT_CHOICES = (
		('b', 'box Office'),	
		('t', "Top250"),	
		('p', "Popular"),	 
	)
    image = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    weekend = models.CharField(max_length=10)
    gross = models.CharField(max_length=10)
    weeks = models.CharField(max_length=3)
    category = models.CharField(max_length=1, choices=CAT_CHOICES, verbose_name='Category')

    def __str__(self):
        return self.title