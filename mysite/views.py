from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    context = {
        'title': 'Hello!',
    }
    return render(request, 'home.html', context)