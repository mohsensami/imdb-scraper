from django.shortcuts import render

import requests
from bs4 import BeautifulSoup


def top250Movies(request):
    url = 'http://www.imdb.com/chart/top'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    items = soup.find_all('td', {'class':'posterColumn'})
    context = {'result': items}
    return render(request, 'base.html', context)