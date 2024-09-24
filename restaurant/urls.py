from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('menu/', views.menu_list, name='menu_list'),
    path('inventory/', views.inventory, name='inventory'),
    path('purchase/', views.purchase, name='purchase'),
]