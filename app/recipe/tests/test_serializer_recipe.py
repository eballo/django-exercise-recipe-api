from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer

RECIPE_URL = "/api/recipies/"

def sample_recipe(**params):
    """Create and return a sample recipe for testing"""
    defaults = {
        "name": "Pizza",
        "description": "Put it in the oven"
    }
    defaults.update(params)

    return Recipe.objects.create(**defaults)


class PublicRecipeApiTests(TestCase):
    """ Public recipe API """

    def setUp(self):
        self.client = APIClient()

    def test_create_a_recipe(self):
        """Test creating a recipes POST"""
        
        payload = {
                "name": "Pizza",
                "description": "Put it in the oven",
                "ingredients": [
                                {"name": "dough"}, 
                                {"name": "cheese"},
                                {"name": "tomato"}
                                ]
                }
        
        res = self.client.post(RECIPE_URL, payload)
        #import pdb; pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)


    def test_retrieve_one_recipe(self):
        """Test retriving a list of recipes GET"""
        sample_recipe()

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all()
        serilizer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serilizer.data)

    def test_retrieve_multiple_recipes(self):
        """Test retriving a list of recipes GET"""
        sample_recipe()
        sample_recipe()

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_update_recipe(self):
        """Test update a recipe PATCH"""
        recipe = sample_recipe()
        
        payload = {
            "name": "Pizza",
            "description": "Put it in the oven",
            "ingredients": [
                            {"name": "dough"}, 
                            {"name": "cheese"},
                            {"name": "tomato"}
                            ]
            }

        res = self.client.patch(RECIPE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
