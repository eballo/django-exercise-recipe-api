from rest_framework import status
from rest_framework.test import APITestCase
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


class PublicRecipeApiTests(APITestCase):
    """ Public recipe API """

    def test_create_a_recipe(self):
        """Test creating a recipes POST"""

        payload = {"name": "Pizza",
                   "description": "Put it in the oven",
                   "ingredients": [
                       {"name": "dough"},
                       {"name": "cheese"},
                       {"name": "tomato"}]}

        res = self.client.post(RECIPE_URL,
                               payload,
                               format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        self.assertEqual(res.data['name'], recipe.name)
        self.assertEqual(res.data['description'], recipe.description)

    def test_retrieve_multiple_recipes(self):
        """Test retriving a list of recipes GET"""

        sample_recipe()
        sample_recipe()

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(len(res.data), 2)

    def test_retrieve_one_recipe(self):
        """Test retriving one recipe GET"""

        recipe = sample_recipe()
        get_url = "/api/recipes/" + str(recipe.id) + "/"

        res = self.client.get(get_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], recipe.name)
        self.assertEqual(res.data['description'], recipe.description)

    def test_update_recipe(self):
        """Test update a recipe PATCH"""
        # create a recipe
        recipe = sample_recipe()

        patch_url = "/api/recipes/" + str(recipe.id) + "/"
        payload = {"name": "Salty Pizza",
                   "description": "Put it in the oven",
                   "ingredients": [{"name": "salt"}, {"name": "olives"}]}

        # update the created recipe
        res = self.client.patch(patch_url,
                                payload,
                                format="json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        recipe = Recipe.objects.get(id=recipe.id)
        self.assertEqual(recipe.name, "Salty Pizza")

    def test_delete_recipe(self):
        """Test delete a recipe DELETE"""
        # create a recipe
        recipe = sample_recipe()

        delete_url = "/api/recipes/" + str(recipe.id) + "/"

        # delete the created recipe
        res = self.client.delete(delete_url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Recipe.objects.filter(id=recipe.id).exists())
        # OLD CODE
        #self.assertRaises(Recipe.DoesNotExist,
        #                  Recipe.objects.get,
        #                  id=recipe.id)
