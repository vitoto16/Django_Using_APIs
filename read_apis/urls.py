from django.urls import path
from .views import django_blog_view, appreceitas_view, general_view

urlpatterns = [
    path('', general_view.index, name='index'),
]