from django.urls import path
from . import views

#this "namesapce" allows the html to call a specific view according to this name
app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
]