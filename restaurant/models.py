from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price_per_unit = models.FloatField()

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
