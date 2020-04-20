import uuid
import os
from django.db import models


def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]  # returns the extension of the file name
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)


class Ingredient(models.Model):
    """Ingredient to be used in a Recipe"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Recipe model object"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    time_minutes = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    link = models.CharField(max_length=255, blank=True)
    ingredients = models.ManyToManyField('Ingredient')
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self):
        return self.name
