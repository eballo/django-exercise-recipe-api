from django.test import TestCase

from recipe import models


class ModelRecipeTests(TestCase):

    def test_recipe_str(self):
        """
        Test the recipe model string representation
        """
        recipe = models.Recipe.objects.create(
            name='Cheese cake',
            description="A delicious cheese cake!"
        )

        self.assertEqual(str(recipe), recipe.name)

    def test_one_ingredients_str(self):
        """
        Test one ingredients model string representation
        """
        recipe = models.Recipe.objects.create(
            name='Cheese cake',
            description="A delicious cheese cake!"
        )

        ingredient = models.Ingredient.objects.create(
            name='cheese',
            recipe=recipe
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_two_ingredients_one_recipe(self):
        """
        Test two ingredients model string representation
        """
        recipe = models.Recipe.objects.create(
            name='Cheese cake',
            description="A delicious cheese cake!"
        )

        ingredient1 = models.Ingredient.objects.create(
            name='oil',
            recipe=recipe
        )

        ingredient2 = models.Ingredient.objects.create(
            name='cheese',
            recipe=recipe
        )

        self.assertEqual(str(ingredient1), ingredient1.name)
        self.assertEqual(str(ingredient2), ingredient2.name)

    def test_two_recipes_one_ingredient(self):
        """
        Test two recipes and one ingredient
        """
        recipe1 = models.Recipe.objects.create(
            name='Cheese cake1',
            description="A delicious cheese cake1!"
        )

        recipe2 = models.Recipe.objects.create(
            name='Cheese cake2',
            description="A delicious cheese cake2!"
        )

        ingredient1 = models.Ingredient.objects.create(
            name='cheese',
            recipe=recipe1
        )

        ingredient2 = models.Ingredient.objects.create(
            name='cheese',
            recipe=recipe2
        )

        self.assertEqual(str(ingredient1), ingredient1.name)
        self.assertEqual(str(ingredient2), ingredient2.name)
