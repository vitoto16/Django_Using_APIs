import requests
from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(720)
def receitas_index(request):
    response = requests.get('https://appreceitas.herokuapp.com/api/lista-receitas/')
    appreceitas_api_data = response.json()

    api_data = {
            'recipes': appreceitas_api_data,
        }

    return render(request, 'receitas/receitas.html', api_data)

