from django.http import HttpResponse
from rest_framework import viewsets

from recipe.serializers import RecipeSerializer
from recipe.models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    """ Manage a Recipe in the database """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request):
        return HttpResponse('list')

    def create(self, request, *args, **kwargs):
        return HttpResponse('create')

    def retrieve(self, request):
        return HttpResponse('retrieve')

    def update(self, request):
        return HttpResponse('update')

    def partial_update(self, request):
        return HttpResponse('partial')

    def destroy(self, request):
        return HttpResponse('destroy')
