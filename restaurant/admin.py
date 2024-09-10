from django.contrib import admin

from restaurant.models import Ingredient, MenuItem, RecipeRequirement, Purchase

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)

