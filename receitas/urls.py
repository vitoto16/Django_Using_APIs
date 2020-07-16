from django.urls import path
from read_apis.views import appreceitas_view

urlpatterns = [
    path('', appreceitas_view.receitas_index, name='receitas-index')
]