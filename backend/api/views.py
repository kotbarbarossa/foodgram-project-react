from rest_framework import permissions, viewsets, mixins
from .serializers import UserSerializer
from users.models import User
from recipes.models import Recipe
from ingredients.models import Ingredient
from tags.models import Tag
from .serializers import RecipeReadSerializer, IngredientSerializer, TagSerializer, RecipeWriteSerializer





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class IngredientTagViewSet(viewsets.ModelViewSet):
    """Кастомный класс для ингредиентов и тэгов."""
    # permission_classes = (IsAdminOrReadOnly,)
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    # search_fields = (
    #     'name',
    #     'slug',
    #     )
    # pagination_class = LimitOffsetPagination
    # lookup_field = 'slug'


class IngredientViewSet(IngredientTagViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(IngredientTagViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """ none """
    def get_queryset(self):
        return Recipe.objects.all()
    # permission_classes = (IsAdminOrReadOnly,)
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = TitleFilter
    # ordering_fields = ('name',)
    # ordering = ('name',)

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH', 'PUT',):
            return RecipeWriteSerializer
        return RecipeReadSerializer