from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Главная',
        'values': ['some', 'hello', '123'],
        'obj': {
            'car': 'bmw',
            'age': 18,
            'hobby': 'fb',
        },
        'var': 'variable'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')