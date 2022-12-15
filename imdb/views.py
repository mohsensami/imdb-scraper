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
        for item in row.find_all('td'):
            for d in item.find_all('td'):
                print(d.find('td', {'class':'weeksColumn'}))
            # obj, created = Movie.objects.get_or_create(
            #     image = item.select_one('.posterColumn')['src'],
            #     title = item.select_one('.titleColumn').text,
            #     slug = slugify(item.select_one('.titleColumn').text),
            #     weekend = item.select_one('.ratingColumn').text,
            #     gross = item.select_one('.ratingColumn.secondaryInfo').text,
            #     weeks = item.select_one('.weeksColumn').text,
            # )
            # data.append(obj)
    context = {'result': data}
    return render(request, 'base.html', context)
