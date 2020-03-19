from django.db import models


class Recipe(models.Model):
    """Recipe model object"""
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient to be used in a Recipe"""
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    def __str__(self):
        return self.name
