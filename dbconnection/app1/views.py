from django.shortcuts import render
from .models import student
# Create your views here.

def register(request):
    if request.method == "POST":
        name= request.POST.get("name")
        lname= request.POST.get("lname")

        # inserted data into student table
        student.objects.create(
            name= name,
            lname= lname
        )
    return render(request, "app1/register.html")



def get_data(request):
    data= student.objects.all()
    return render(request, "app1/op.html", {"data": data})

def get_data_one(request):
    data= student.objects.get(id=1)
    return render(request,  "app1/op.html", {"new": data})


