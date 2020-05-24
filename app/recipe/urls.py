from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe.views import RecipeViewSet, RecipeDetailsViewSet, TagViewSet, IngredientViewSet

router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("ingredients", IngredientViewSet)
router.register("details", RecipeDetailsViewSet)
router.register("", RecipeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
