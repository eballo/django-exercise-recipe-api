from rest_framework import serializers
from recipe.models import Ingredient, Recipe

# Ref documentation:
# https://www.django-rest-framework.org/api-guide/serializers/


class IngredientSerializer(serializers.ModelSerializer):
    """ Serializer for Ingredients Objects """

    class Meta:
        model = Ingredient
        fields = ['name']
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """ Serializer for Recipe Objects """

    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'ingredients']
        read_only_fields = ('id',)

    def __create_ingredients(self, ingredients, recipe):
        for ingredient in ingredients:
            Ingredient.objects.create(
                name=ingredient['name'],
                recipe=recipe
            )

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')

        recipe = Recipe.objects.create(
            name=validated_data['name'],
            description=validated_data['description']
        )

        self.__create_ingredients(ingredients, recipe)
        return recipe

    def update(self, recipe, validated_data):
        ingredients = validated_data.pop('ingredients')

        recipe = super().update(recipe, validated_data)
        recipe.save()

        # NOTE: Before I was doing this:
        # recipe.name = validated_data['name']
        # recipe.description = validated_data['description']
        # but is better to use:
        # recipe = super().update(recipe, validated_data)

        recipe.ingredients.all().delete()
        self.__create_ingredients(ingredients, recipe)

        return recipe
