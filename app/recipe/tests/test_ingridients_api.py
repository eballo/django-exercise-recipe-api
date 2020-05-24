from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from recipe.models import Ingredient, Recipe
from recipe.serializers import IngredientSerializer


INGREDIENTS_URL = "/api/recipes/ingredients/"


class PublicIngredientsApiTest(TestCase):
    """Test the private available Ingredients API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_ingridients_list(self):
        """Test that retrieve a list of ingredients"""
        Ingredient.objects.create(name="Banana")
        Ingredient.objects.create(name="Salt")

        res = self.client.get(INGREDIENTS_URL)

        ingredients = Ingredient.objects.all().order_by("-name")
        serializer = IngredientSerializer(ingredients, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_ingredient_successful(self):
        """Test creating a new ingredient"""
        payload = {"name": "Test ingredient"}
        self.client.post(INGREDIENTS_URL, payload)

        exists = Ingredient.objects.filter(name=payload["name"]).exists()
        self.assertTrue(exists)

    def test_create_ingredient_invalid(self):
        """Test creating a new ingredient with invalid payload"""
        payload = {"name": ""}
        res = self.client.post(INGREDIENTS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_ingredients_assigned_to_recipies(self):
        """Test filtering ingredients by those assinged to recipies"""
        ingredient1 = Ingredient.objects.create(name="Apples")
        ingredient2 = Ingredient.objects.create(name="Turkey")
        recipe = Recipe.objects.create(
            name="Apple crumble", description="delicious apple crumble", time_minutes=10, price=5.0,
        )
        recipe.ingredients.add(ingredient1)

        res = self.client.get(INGREDIENTS_URL, {"assigned_only": 1})

        serializer1 = IngredientSerializer(ingredient1)
        serializer2 = IngredientSerializer(ingredient2)
        self.assertIn(serializer1.data, res.data)
        self.assertNotIn(serializer2.data, res.data)

    def test_retrieve_ingredients_assigned_unique(self):
        """Test filtering ingredients by assigned returns unique items"""
        ingredient = Ingredient.objects.create(name="Eggs")
        Ingredient.objects.create(name="Cheese")

        recipe = Recipe.objects.create(name="Eggs benedict", description="delicious eggs", time_minutes=30, price=3.0,)
        recipe.ingredients.add(ingredient)

        recipe2 = Recipe.objects.create(
            name="Coriander eggs on toast", description="delicious eggs", time_minutes=225, price=5.0,
        )
        recipe2.ingredients.add(ingredient)

        res = self.client.get(INGREDIENTS_URL, {"assigned_only": 1})

        self.assertEqual(len(res.data), 1)
