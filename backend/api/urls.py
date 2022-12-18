from django.urls import include, path
from rest_framework import routers
from .views import (
    UserViewSet,
    RecipeViewSet,
    IngredientViewSet,
    TagViewSet,
)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'recipies', RecipeViewSet, basename='recipies')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
