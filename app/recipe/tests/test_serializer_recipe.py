from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer

RECIPE_URL = "/api/recipes/"

# NOTES:
# To Debug --> import pdb; pdb.set_trace()


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

        payload = ('{"name": "Pizza", '
                   '"description": "Put it in the oven", '
                   '"ingredients": [{"name": "dough"}, '
                   '{"name": "cheese"},{"name": "tomato"}]}')

        res = self.client.post(RECIPE_URL,
                               payload,
                               content_type="application/json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_retrieve_multiple_recipes(self):
        """Test retriving a list of recipes GET"""
        sample_recipe()
        sample_recipe()

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_one_recipe(self):
        """Test retriving one recipe GET"""
        recipe = sample_recipe()
        get_url = "/api/recipes/" + str(recipe.id) + "/"

        res = self.client.get(get_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_recipe(self):
        """Test update a recipe PATCH"""
        # create a recipe
        recipe = sample_recipe()

        patch_url = "/api/recipes/" + str(recipe.id) + "/"
        payload = ('{ "name": "Salty Pizza",'
                   '"description": "Put it in the oven",'
                   '"ingredients": [ {"name": "salt"}, {"name": "olives"}]}')

        # update the created recipe
        res = self.client.patch(patch_url,
                                payload,
                                content_type="application/json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_recipe(self):
        """Test update a recipe PATCH"""
        # create a recipe
        recipe = sample_recipe()

        delete_url = "/api/recipes/" + str(recipe.id) + "/"

        # delete the created recipe
        res = self.client.delete(delete_url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
