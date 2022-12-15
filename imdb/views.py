from django.shortcuts import render
from .models import Movie

import requests
from bs4 import BeautifulSoup


def top250Movies(request):
    url = 'https://www.imdb.com/chart/boxoffice'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data= {}
    title = soup.find('h1').text
    # sub_title = soup.find('h4').text
    data['title'] = title
    # data['sub_title'] = sub_title

    table = soup.find('table')
    rows = table.find_all('tr')
    for row in rows:
        for head in row.find_all('td', {'class':'titleColumn'}):
            Movie(
                tite = head.text
            ).save()
            # print(head.text)


    # rows = table.find('tr')
    # for row in rows:
    #     for head in row.find_all('th'):
    #         heads = head.text
    #         data.append(heads)
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