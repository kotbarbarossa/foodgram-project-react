from rest_framework import permissions, viewsets, mixins, status, filters
from .serializers import UserSerializer
from users.models import User
from recipes.models import Recipe, FavoriteRecipe, ShoppingCart
from ingredients.models import Ingredient
from tags.models import Tag
from .serializers import RecipeReadSerializer, IngredientSerializer, TagSerializer, RecipeWriteSerializer
from rest_framework.permissions import (SAFE_METHODS, AllowAny,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        )
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend



class UserViewSet(viewsets.ModelViewSet):
    """User ViewSet."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class IngredientTagViewSet(viewsets.ModelViewSet):
    """Ingredient and Tag mixin ViewSet."""
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',) 


class IngredientViewSet(IngredientTagViewSet):
    """Ingredient ViewSet."""    
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(IngredientTagViewSet):
    """Tag mixin ViewSet."""    
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """Recipe ViewSet."""
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('name', 'ingredients', 'tags', 'author')
    search_fields = ('name',)
    ordering_fields = ('name',)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecipeReadSerializer
        return RecipeWriteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                'Recipe deleted successfully.'
            }, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({
                f'The wind blows from the void.'
            }, status=status.HTTP_400_BAD_REQUEST)
