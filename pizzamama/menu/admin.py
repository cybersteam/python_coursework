from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ("name", "ingredients", "price", "vegetarian", "glutenfree" )
    search_fields = ("name", "price")


# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
