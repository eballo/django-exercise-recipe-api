from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from recipe.models import Tag, Recipe
from recipe.serializers import TagSerializer


TAGS_URL = "/api/recipes/tags/"


class PublicTagsApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_tags(self):
        """Test retrieving tags"""
        Tag.objects.create(name="Vegan")
        Tag.objects.create(name="Dessert")

        res = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by("-name")
        serializer = TagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_tag_successful(self):
        """Test creating a new tag"""
        payload = {"name": "Test tag"}
        self.client.post(TAGS_URL, payload)

        exists = Tag.objects.filter(name=payload["name"]).exists()
        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """Test creating a new tag with invalid payload"""
        payload = {"name": ""}
        res = self.client.post(TAGS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_tags_assigned_to_recipies(self):
        """Test filtering tags by those assinged to recipies"""
        tag1 = Tag.objects.create(name="Breakfast")
        tag2 = Tag.objects.create(name="Lunch")
        recipe = Recipe.objects.create(name="Coriander eggs on toast", description="test", time_minutes=10, price=5.0)
        recipe.tags.add(tag1)

        res = self.client.get(TAGS_URL, {"assigned_only": 1})

        serializer1 = TagSerializer(tag1)
        serializer2 = TagSerializer(tag2)
        self.assertIn(serializer1.data, res.data)
        self.assertNotIn(serializer2.data, res.data)

    def test_retrieve_tags_assigned_unique(self):
        """Test filtering tags by assigned returns unique items"""
        tag = Tag.objects.create(name="Breakfast")
        Tag.objects.create(name="Lunch")

        recipe1 = Recipe.objects.create(name="Pancakes", description="pancake big", time_minutes=5, price=3.0,)
        recipe1.tags.add(tag)

        recipe2 = Recipe.objects.create(name="Porridge", description="pancake small", time_minutes=5, price=2.0,)
        recipe2.tags.add(tag)

        res = self.client.get(TAGS_URL, {"assigned_only": 1})

        self.assertEqual(len(res.data), 1)
