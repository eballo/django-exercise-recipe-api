from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

from recipe.serializers import RecipeSerializer, TagSerializer, \
     IngredientSerializer, RecipeDetailSerializer, RecipeImageSerializer
from recipe.models import Recipe, Tag, Ingredient

# Ref Documentation:
# https://www.django-rest-framework.org/api-guide/filtering/


class BaseRecipeAttributesSet(viewsets.GenericViewSet,
                              mixins.ListModelMixin,
                              mixins.CreateModelMixin):
    """Base class for common logic in the recipe attributes"""

    def get_queryset(self):
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(recipe__isnull=False)

        return queryset.order_by('-name').distinct()


class TagViewSet(BaseRecipeAttributesSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(BaseRecipeAttributesSet):
    """Manage Ingredient in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """ Manage a Recipe in the database """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def _params_to_ints(self, qs):
        """Convert a list of strings IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        tags = self.request.query_params.get('tags')
        ingredients = self.request.query_params.get('ingredients')
        queryset = self.queryset
        if tags:
            tag_ids = self._params_to_ints(tags)
            queryset = queryset.filter(tags__id__in=tag_ids)

        if ingredients:
            ingredients_ids = self._params_to_ints(ingredients)
            queryset = queryset.filter(ingredients__id__in=ingredients_ids)

        return queryset.order_by('-id')

    def get_serializer_class(self):
        """Return appropiate serializer class"""
        if self.action == 'retrieve':
            return RecipeDetailSerializer
        elif self.action == 'upload_image':
            return RecipeImageSerializer

        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to a recipe"""
        recipe = self.get_object()
        serializer = self.get_serializer(
            recipe,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def list(self, request):
        query = request.query_params
        if 'name' in query:
            self.queryset = self.queryset.filter(name__icontains=query['name'])

        return super().list(request)
