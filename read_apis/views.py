from django.shortcuts import render
import requests


def index(request):
    response = requests.get('https://django-blog-corey-tutorial.herokuapp.com/api/posts-list/')
    blog_api_data = response.json()

    response = requests.get('https://appreceitas.herokuapp.com/api/lista-receitas/')
    appreceitas_api_data = response.json()

    api_data = {
        'posts': blog_api_data,
        'recipes': appreceitas_api_data
    }

    return render(request, 'read_apis/index.html', api_data)
