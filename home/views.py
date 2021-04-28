from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("This is the homepage")
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')
