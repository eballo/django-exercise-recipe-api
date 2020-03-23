from django.http import HttpResponse
from rest_framework import viewsets

from recipe.serializers import RecipeSerializer
from recipe.models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    """ Manage a Recipe in the database """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request):
        query = request.query_params
        if('name' in query):
            self.queryset = Recipe.objects.filter(name__contains=query['name'])
        
        return super().list(request)
