from django.shortcuts import render
from restaurant.models import MenuItem


def home(request):
    return render(request, "restaurant/base.html")

def menu_list(request):
    return render(request, 'restaurant/menu_list.html')

def inventory(request):
    return render(request, 'restaurant/inventory.html')

def purchase(request):
    return render(request, 'restaurant/purchase.html')