from django.shortcuts import render
from .models import Movie
from django.utils.text import slugify

import requests
from bs4 import BeautifulSoup

import sys
sys.setrecursionlimit(7500)


def boxOfficeMovies(request):
    url = 'https://imdb-api.com/box-office'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('table')
    # rows = table.find_all('tr')
    data = ''
    # for row in rows:
    #     obj, created = Movie.objects.get_or_create(
    #         image = row.find('td', {'class':'posterColumn'}).find('img')['src'].replace('\n', ''),
    #         title = row.find('td', {'class':'titleColumn'}).text.replace('\n', ''),
    #         slug = slugify(row.find('td', {'class':'titleColumn'}).text.replace('\n', '')),
    #         weekend = row.find('td', {'class':'ratingColumn'}).text.replace('\n', '').strip(),
    #         gross = row.find('td', {'class':'ratingColumn'}).text.replace('\n', '').strip(),
    #         weeks = row.find('td', {'class':'weeksColumn'}).text.replace('\n', ''),
    #         category='b'
    #     )
    #     data.append(obj)
    data += str(table)

    context = {'result': data}
    return render(request, 'table.html', context)


def top250Movies(request):
    url = 'https://imdb-api.com/top-250-movies'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    data = ''
    table = soup.find('table')
    rows = table.find_all('tr')

    # data.append(table)
    data += str(table)

    context = {'result': data}

    return render(request, 'table.html', context)


def boxOfficeAllMovies(request):
    url = 'https://imdb-api.com/box-office-alltime'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    data = ''
    table = soup.find('table')
    rows = table.find_all('tr')

    # data.append(table)
    data += str(table)

    context = {'result': data}

    return render(request, 'table.html', context)


def commingSoonMovies(request):
    url = 'https://imdb-api.com/coming-soon'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    data = ''
    table = soup.find('table')
    rows = table.find_all('tr')

    # data.append(table)
    data += str(table)

    context = {'result': data}

    return render(request, 'table.html', context)


def inTheaters(request):
    url = 'https://imdb-api.com/in-theaters'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    data = ''
    table = soup.find('table')
    rows = table.find_all('tr')

    # data.append(table)
    data += str(table)

    context = {'result': data}

    return render(request, 'table.html', context)


def popularMovies(request):
    url = 'https://imdb-api.com/most-popular-movies'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    data = ''
    table = soup.find('table')
    rows = table.find_all('tr')

    # data.append(table)
    data += str(table)

    context = {'result': data}

    return render(request, 'table.html', context)