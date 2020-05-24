import os
import tempfile
from unittest import TestCase

from PIL import Image
from rest_framework import status
from rest_framework.test import APIClient
from recipe.serializers import RecipeSerializer
from recipe.tests.test_recipe_api import sample_recipe, sample_tag, RECIPE_URL, sample_ingredient


def image_upload_url(recipe_id):
    """Return URL for recipe image upload"""
    return "/api/recipes/" + str(recipe_id) + "/upload-image/"


class RecipeImageUploadTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.recipe = sample_recipe()

    def tearDown(self):
        self.recipe.image.delete()

    def test_upload_image_to_recipe(self):
        """Test uploading an image to recipe"""
        url = image_upload_url(self.recipe.id)
        with tempfile.NamedTemporaryFile(suffix=".jpg") as ntf:
            img = Image.new("RGB", (10, 10))
            img.save(ntf, format="JPEG")
            ntf.seek(0)  # Seek the pointer to the begining of the file
            res = self.client.post(url, {"image": ntf}, format="multipart")

            self.recipe.refresh_from_db()
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertIn("image", res.data)
            self.assertTrue(os.path.exists(self.recipe.image.path))

    def test_upload_image_bad_request(self):
        """Test uploading an invalid image"""
        url = image_upload_url(self.recipe.id)
        res = self.client.post(url, {"image": "notimage"}, format="multipart")

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_filter_recipes_by_tags(self):
        """Test returning recipes with specific tags"""
        recipe1 = sample_recipe(name="Thai vegetable curry")
        recipe2 = sample_recipe(name="Aubergine with tahini")
        tag1 = sample_tag(name="Vegan")
        tag2 = sample_tag(name="Vegetarian")
        recipe1.tags.add(tag1)
        recipe2.tags.add(tag2)
        recipe3 = sample_recipe(name="Fish and chips")

        res = self.client.get(RECIPE_URL, {"tags": f"{tag1.id}, {tag2.id}"})

        serializer1 = RecipeSerializer(recipe1)
        serializer2 = RecipeSerializer(recipe2)
        serializer3 = RecipeSerializer(recipe3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)

    def test_filter_recipes_by_ingredients(self):
        """Test returning recipes with specific ingredients"""
        recipe1 = sample_recipe(name="Posh beans on toast")
        recipe2 = sample_recipe(name="Chicken cacciatore")
        ingredient1 = sample_ingredient(name="Feta cheese")
        ingredient2 = sample_ingredient(name="Chicken")
        recipe1.ingredients.add(ingredient1)
        recipe2.ingredients.add(ingredient2)
        recipe3 = sample_recipe(name="Steak and Mushroom")

        res = self.client.get(RECIPE_URL, {"ingredients": f"{ingredient1.id}, {ingredient2.id}"})

        serializer1 = RecipeSerializer(recipe1)
        serializer2 = RecipeSerializer(recipe2)
        serializer3 = RecipeSerializer(recipe3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)
