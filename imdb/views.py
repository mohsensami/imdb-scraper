from django.shortcuts import render
from .models import Movie
from django.utils.text import slugify

import requests
from bs4 import BeautifulSoup


def top250Movies(request):
    url = 'https://www.imdb.com/chart/boxoffice'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')
    data = []
    for row in rows:
        for item in row.find_all('td', {'class':'titleColumn'}):
            obj, created = Movie.objects.get_or_create(
                title = item.text,
                slug = slugify(item.text)
            )
            data.append(obj)
            # print(obj)
    context = {'result': data}
    return render(request, 'base.html', context)
