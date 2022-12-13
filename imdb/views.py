from django.shortcuts import render


def top250Movies(request):
    return render(request, 'base.html')