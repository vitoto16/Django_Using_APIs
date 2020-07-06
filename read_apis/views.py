from django.shortcuts import render
import requests


def index(request):
    response = requests.get('https://django-blog-corey-tutorial.herokuapp.com/api/posts-list/')
    api_data = {
        'posts': response.json()
    }

    return render(request, 'read_apis/index.html', api_data)
