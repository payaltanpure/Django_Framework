from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#home
def home(request):
    return HttpResponse("I am home page of app2!")


