from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#home
def home(request):
    return HttpResponse("I am home page of app2!")


def home_html(request):
    if request.method=="POST":
        uname= request.POST.get("fname")
        return render (request, "home.html", {"name":uname})

def view_form(request):
    return render(request, "home.html")
