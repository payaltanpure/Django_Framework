from django.shortcuts import render

def ex1(request):
    data={
        "age": 12
    }
    return render(request, "index.html", data)

def ex2(request, marks):
    data={
        "marks": marks
    }
    return render(request, "index.html", data)

def ex3(request, name):
    data={
        "name": name
    }
    return render(request, "index.html", data)

def ex4(request):
    data={
        "list":[10,20,30,40,50],
        "names": ['Payal' ,'Anu', 'Shiv'],
        "fruitname": ['Apple', 'Mango', 'Peru'],
        "carname": ('Mercedes', 'BMW', 'XUV 700'),


    }
    return render(request, "loop.html", data)