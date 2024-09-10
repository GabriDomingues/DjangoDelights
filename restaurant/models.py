from django.db import models
from rest_framework import serializers


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price_per_unit = models.FloatField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.menu_item} - {self.ingredient} - {self.quantity}"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'price']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'price_per_unit']

class RecipeRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeRequirement
        fields = ['menu_item', 'ingredient', 'quantity']

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['menu_item', 'timestamp']