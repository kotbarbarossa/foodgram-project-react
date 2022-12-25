from rest_framework import viewsets, status, filters, generics
from .serializers import UserSerializer
from users.models import User
from recipes.models import Recipe
from ingredients.models import Ingredient
from tags.models import Tag
from .serializers import (
    RecipeReadSerializer,
    IngredientSerializer,
    TagSerializer,
    RecipeWriteSerializer,
    RecipeSubscribeSerializer,
    SubscribeSerializer,
    )
from rest_framework.permissions import (
                                        SAFE_METHODS,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        )
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    """User ViewSet."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


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
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
        except Exception:
            return Response({
                'The wind blows from the void.'
            }, status=status.HTTP_400_BAD_REQUEST)


class GetObjectMixin(
        generics.CreateAPIView,
        generics.DestroyAPIView):
    """AddDeleteFavoriteRecipe and AddDeleteShoppingCart mixin ViewSet."""

    serializer_class = RecipeSubscribeSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        recipe_id = self.kwargs['recipe_id']
        recipe = get_object_or_404(Recipe, id=recipe_id)
        self.check_object_permissions(self.request, recipe)
        return recipe


class AddDeleteFavoriteRecipe(GetObjectMixin):
    """AddDeleteFavoriteRecipe ViewSet."""

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        request.user.favorite_recipe.recipes.add(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        request.user.favorite_recipe.recipes.remove(instance)
        return Response({
                'Recipe removed from favorites.'
            }, status=status.HTTP_204_NO_CONTENT)


class AddDeleteShoppingCart(GetObjectMixin):
    """AddDeleteShoppingCart ViewSet."""

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        request.user.shopping_cart.recipes.add(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        request.user.shopping_cart.recipes.remove(instance)
        return Response({
                'Recipe removed from shoping cart.'
            }, status=status.HTTP_204_NO_CONTENT)


class AddAndDeleteSubscribe(
        generics.DestroyAPIView,
        generics.CreateAPIView,
        generics.ListAPIView):
    """AddAndDeleteSubscribe ViewSet."""

    serializer_class = SubscribeSerializer

    def get_queryset(self):
        return self.request.user.follower.all()

    def get_object(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(self.request, user)
        return user

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id == instance.id:
            return Response(
                {'errors': "You can't subscribe to yourself."},
                status=status.HTTP_400_BAD_REQUEST)
        if request.user.follower.filter(author=instance).exists():
            return Response(
                {'errors': 'You are already subscribed to this author.'},
                status=status.HTTP_400_BAD_REQUEST)
        subs = request.user.follower.create(author=instance)
        serializer = self.get_serializer(subs)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance):
        self.request.user.follower.filter(author=instance).delete()
