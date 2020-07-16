from django.shortcuts import render

def index(request):
    return render(request, 'read_apis/index.html')