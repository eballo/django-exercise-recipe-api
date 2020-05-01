from rest_framework import status
from rest_framework.test import APITestCase
from recipe.models import Recipe, Ingredient, Tag
from recipe.serializers import RecipeSerializer, RecipeDetailSerializer

RECIPE_URL = "/api/recipes/"

# NOTES:
# To Debug --> import pdb; pdb.set_trace()


def detail_url(recipe_id):
    """Return recipe detail URL"""
    return "/api/recipes/" + str(recipe_id) + "/"


def sample_tag(name="Main course"):
    """Create and return a sample tag"""
    return Tag.objects.create(name=name)


def sample_ingredient(name="Cinnamon"):
    """Create and return a sample ingredient"""
    return Ingredient.objects.create(name=name)


def sample_recipe(**params):
    """Create and return a sample recipe for testing"""
    defaults = {
        "name": "Pizza",
        "description": "Put it in the oven",
        "time_minutes": 10,
        "price": 2.0
    }
    defaults.update(params)

    return Recipe.objects.create(**defaults)


class PublicRecipeApiTests(APITestCase):
    """ Public recipe API """

    def test_create_a_recipe(self):
        """Test creating a recipes POST"""

        payload = {"name": "Pizza",
                   "description": "Put it in the oven",
                   "ingredients": [],
                   "tags": []}

        res = self.client.post(RECIPE_URL,
                               payload,
                               format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        self.assertEqual(res.data['name'], recipe.name)
        self.assertEqual(res.data['description'], recipe.description)
        self.assertEqual(res.data['time_minutes'], recipe.time_minutes)
        self.assertEqual(res.data['price'], recipe.price)

    def test_retrieve_multiple_recipes(self):
        """Test retrieving a list of recipes GET"""

        sample_recipe()
        sample_recipe()

        res = self.client.get(RECIPE_URL)

        recipes = Recipe.objects.all().order_by('-id')
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

    def test_filter_recipe(self):
        """Test filtering a recipe GET"""

        sample_recipe(name="Tortilla", description="easy and tasty")
        sample_recipe(name="Pasta", description="best pasta ever")
        sample_recipe(name="Pizza", description="best pizza ever")

        get_url = "/api/recipes/?name=Pi"

        res = self.client.get(get_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], "Pizza")
        self.assertEqual(res.data[0]['description'], "best pizza ever")

    def test_create_recipe_with_tags(self):
        """Test creating a recipe with tags"""
        tag1 = sample_tag(name='Vegan')
        tag2 = sample_tag(name='Dessert')
        payload = {
            'name': 'Avocado lime cheesecake',
            'description': 'small description',
            'tags': [tag1.id, tag2.id],
            'ingredients': [],
            'time_minutes': 60,
            'price': 20.00
        }
        res = self.client.post(RECIPE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        tags = recipe.tags.all()

        self.assertEqual(tags.count(), 2)
        self.assertIn(tag1, tags)
        self.assertIn(tag2, tags)

    def test_create_recipe_with_ingredients(self):
        """Test creating recipe with ingredients"""
        ingredient1 = sample_ingredient(name='Prawns')
        ingredient2 = sample_ingredient(name='Ginger')
        payload = {
            'name': 'Thai prawn red curry',
            'description': 'small description',
            'ingredients': [ingredient1.id, ingredient2.id],
            'time_minutes': 20,
            'price': 7.00,
            "tags": []
        }
        res = self.client.post(RECIPE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        ingredients = recipe.ingredients.all()

        self.assertEqual(ingredients.count(), 2)
        self.assertIn(ingredient1, ingredients)
        self.assertIn(ingredient2, ingredients)

    def test_view_recipe_details(self):
        """Test viewing a recipe detail"""
        recipe = sample_recipe()
        recipe.tags.add(sample_tag())
        recipe.ingredients.add(sample_ingredient())

        url = detail_url(recipe.id)
        res = self.client.get(url)
        serializer = RecipeDetailSerializer(recipe)
        self.assertEqual(res.data, serializer.data)

    def test_update_recipe(self):
        """Test update a recipe PATCH"""
        # create a recipe
        recipe = sample_recipe()
        new_tag = sample_tag(name='Curry')

        patch_url = "/api/recipes/" + str(recipe.id) + "/"
        payload = {"name": "Salty Pizza",
                   "description": "Put it in the oven",
                   "ingredients": [],
                   "tags": [new_tag.id]}

        # update the created recipe
        res = self.client.patch(patch_url,
                                payload,
                                format="json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        recipe.refresh_from_db()

        self.assertEqual(recipe.name, "Salty Pizza")
        tags = recipe.tags.all()
        self.assertEqual(len(tags), 1)
        self.assertIn(new_tag, tags)

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
        # self.assertRaises(Recipe.DoesNotExist,
        #                  Recipe.objects.get,
        #                  id=recipe.id)
