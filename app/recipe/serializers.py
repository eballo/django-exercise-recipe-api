from rest_framework import serializers
from . import models


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ['name']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = models.Recipe
        fields = ['id', 'name', 'description', 'ingredients']
