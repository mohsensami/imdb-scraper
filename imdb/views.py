from django.shortcuts import render
from .models import Movie
from django.utils.text import slugify

import requests
from bs4 import BeautifulSoup


def top250Movies(request):
    url = 'http://www.imdb.com/chart/boxoffice'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')
    data = []
    for row in rows:
        obj, created = Movie.objects.get_or_create(
            image = row.find('td', {'class':'posterColumn'}).find('img')['src'].replace('\n', ''),
            title = row.find('td', {'class':'titleColumn'}).text.replace('\n', ''),
            slug = slugify(row.find('td', {'class':'titleColumn'}).text.replace('\n', '')),
            weekend = row.find('td', {'class':'ratingColumn'}).text.replace('\n', ''),
            gross = row.find('td', {'class':'ratingColumn'}).text.replace('\n', ''),
            weeks = row.find('td', {'class':'weeksColumn'}).text.replace('\n', ''),
        )
        data.append(obj)

    context = {'result': data}
    return render(request, 'base.html', context)
