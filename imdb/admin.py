from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Movie)