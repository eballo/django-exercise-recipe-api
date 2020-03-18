from django.db import models


class Recipe(models.Model):
    """Recipe model object"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient to be used in a Recipe"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name