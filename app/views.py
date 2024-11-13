from django.shortcuts import render
from app.forms import *
from django.http import HttpRequest, HttpResponse
# Create your views here.
def hey_you(request):
    form = heyyou(request.GET)
    if form.is_valid():
        name = form.cleaned_data["x"]
        return render(request, "heyyou.html", {"form": form, "name": name})
    else:
        return render(request,"heyyou.html", {"form": form})


def food(request):
    form = foods(request.GET)
    if form.is_valid():
        fry = form.cleaned_data["fries"]
        drink = form.cleaned_data["drinks"]
        burger = form.cleaned_data["burgers"]
        fryt = fry * 1.50
        burgert = burger * 4.5
        
        
        total = fryt + drink + burgert
        return render(request, "order.html", {"form": form, "fry": fry, "drink": drink, "burger": burger, "total": total})
    else:

        return render(request,"order.html", {"form":form})
    
def age(request):
    form = ages(request.GET)
    if form.is_valid():
        birth = form.cleaned_data["birthyear"]
        cur = form.cleaned_data["cur_year"]
        total = cur - birth
        return render(request, "age.html", {"form": form, "birth": birth, "cur":cur, "total":total})
    else:
       birth =None
       cur = None
       total = None
       return render(request,"age.html", {"form":form})

