from django.shortcuts import render

# only needed if you use the HttpResponse class
#from django.http import HttpResponse


# Create your views here.



### this will change to return the render like the menu view file.. then you'll need to load the app in the settings file too..
def  index(request):
    return render(request, "main/index.html")
