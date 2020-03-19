from django.http import HttpResponse
from rest_framework import viewsets

from . import serializers
from . import models


class RecipeViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

    def list(self, request):
        return HttpResponse('list')

    def create(self, request):
        return HttpResponse('create')

    def retrieve(self, request, pk=None):
        return HttpResponse('retrieve')

    def update(self, request, pk=None):
        return HttpResponse('update')

    def partial_update(self, request, pk=None):
        return HttpResponse('partial')

    def destroy(self, request, pk=None):
        return HttpResponse('destroy')
