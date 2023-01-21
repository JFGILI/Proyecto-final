from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render (request, 'index.html', context={})

def aboutme(request):
    return render (request, 'aboutme.html', context={})






