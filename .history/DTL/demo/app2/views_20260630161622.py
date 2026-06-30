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
    return render(request, "home.html")


#view calculator
def view_cal(request):
    return render(request, "calci.html")

def calculation(request):
    if request.method== "POST":
        num1= int(request.POST.get("num1"))
        num2= int(request.POST.get("num2"))
        op= num1+num2
        # print(op)
        data={
            "num1":num1,
            "num2":num2,
            "op":op
        }
        return render(request,"calci.html",data)