from django.contrib.auth.views import LoginView
from django.shortcuts import render


def home(request):
    return render(request, "restaurant/base.html")

def menu_list(request):
    return render(request, 'restaurant/menu_list.html')

def inventory(request):
    return render(request, 'restaurant/inventory.html')

def purchase(request):
    return render(request, 'restaurant/purchase.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
