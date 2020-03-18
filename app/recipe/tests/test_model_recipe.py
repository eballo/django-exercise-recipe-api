from django.test import TestCase

from recipe import models


class ModelRecipeTests(TestCase):

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            name='Cheese cake',
            description="A delicious cheese cake!"
        )

        self.assertEqual(str(recipe), recipe.name)
