from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request, name="index"):
    pizzas = Pizza.objects.all().order_by('price')
    

    # pizzas_names = [pizza.name + " : " + "€" + str(pizza.price) for pizza in  pizzas]
    # pizzas_names_str = ", ".join(pizzas_names)
    
    # title = "Our Pizza's:  "

    # return HttpResponse(title + pizzas_names_str)

    
    return render(request, "menu/index.html", {'pizzas': pizzas}) #the 'pizzas' in parenth is the name used in the html file
    
    #{'veg': veg}

    
    
    
