from django.test import TestCase

from recipe.models import Recipe, Ingredient


class ModelRecipeTests(TestCase):
    def test_recipe_str(self):
        """
        Test the recipe model string representation
        """
        recipe = Recipe.objects.create(name="Cheese cake", description="A delicious cheese cake!")

        self.assertEqual(str(recipe), recipe.name)

    def test_one_ingredients_str(self):
        """
        Test one ingredients model string representation
        """
        recipe = Recipe.objects.create(name="Cheese cake", description="A delicious cheese cake!")

        ingredient = Ingredient.objects.create(name="cheese", recipe=recipe)

        self.assertEqual(str(ingredient), ingredient.name)

    def test_two_ingredients_one_recipe(self):
        """
        Test two ingredients model string representation
        """
        recipe = Recipe.objects.create(name="Cheese cake", description="A delicious cheese cake!")

        ingredient1 = Ingredient.objects.create(name="oil", recipe=recipe)

        ingredient2 = Ingredient.objects.create(name="cheese", recipe=recipe)

        self.assertEqual(str(ingredient1), ingredient1.name)
        self.assertEqual(str(ingredient2), ingredient2.name)

    def test_two_recipes_one_ingredient(self):
        """
        Test two recipes and one ingredient
        """
        recipe1 = Recipe.objects.create(name="Cheese cake1", description="A delicious cheese cake1!")

        recipe2 = Recipe.objects.create(name="Cheese cake2", description="A delicious cheese cake2!")

        ingredient1 = Ingredient.objects.create(name="cheese", recipe=recipe1)

        ingredient2 = Ingredient.objects.create(name="cheese", recipe=recipe2)

        self.assertEqual(str(ingredient1), ingredient1.name)
        self.assertEqual(str(ingredient2), ingredient2.name)
