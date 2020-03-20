from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from recipe.models import Recipe

from recipe.serializers import RecipeSerializer

RECIPE_URL = "/api/recipes/"


def sample_recipe(**params):
    """Create and return a sample recipe for testing"""
    defaults = {
        'name': 'Sample recipe name',
        'description': 'Sample recipe description'
    }
    defaults.update(params)

    return Recipe.objects.create(**defaults)


class PublicRecipeApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_one_recipe(self):
        """Test retriving a list of recipes"""
        sample_recipe()

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all()
        serilizer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serilizer.data)

    def test_retrieve_multiple_recipes(self):
        """Test retriving a list of recipes"""
        sample_recipe()
        sample_recipe()

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all()
        serilizer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serilizer.data)
