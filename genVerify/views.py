from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello cert')

def certificate(request, id):
    return HttpResponse(id)