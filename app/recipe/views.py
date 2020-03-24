from rest_framework import viewsets

from recipe.serializers import RecipeSerializer
from recipe.models import Recipe

# Ref Documentation:
# https://www.django-rest-framework.org/api-guide/filtering/


class RecipeViewSet(viewsets.ModelViewSet):
    """ Manage a Recipe in the database """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request):
        query = request.query_params
        if('name' in query):
            self.queryset = self.queryset.filter(name__icontains=query['name'])

        return super().list(request)
