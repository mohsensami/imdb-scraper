from django.shortcuts import render

import requests
from bs4 import BeautifulSoup


def top250Movies(request):
    url = 'https://imdb-api.com/box-office'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('thead')
    rows = table.find('tr')
    for row in rows:
        data = []
        for head in row.find_all('th'):
            heads = head.text
            data.append(heads)
        # for body in row.find_all('td'):
        #     bodies = body.text
        #     data.append(bodies)
    context = {'result': data}
    return render(request, 'base.html', context)



# def top250Movies(request):
#     url = 'https://imdb-api.com/box-office'
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, 'html.parser')
    
#     table = soup.find('table')
#     table_body = table.find('tbody')

#     rows = table_body.find_all('tr')
#     data = []
#     for row in rows:
#         bodies = row.text
#         data.append(bodies)
#     context = {'result': data}
#     return render(request, 'base.html', context)