from django.shortcuts import render
import requests

def receitas_index(request):
    is_cached = ('appreceitas_api_data' in request.session)

    if not is_cached:
        response = requests.get('https://appreceitas.herokuapp.com/api/lista-receitas/')
        request.session['appreceitas_api_data'] = response.json()

    appreceitas_api_data = request.session['appreceitas_api_data']

    api_data = {
            'recipes': appreceitas_api_data,
        }

    return render(request, 'receitas/receitas.html', api_data)

