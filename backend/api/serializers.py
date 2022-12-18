from djoser.serializers import UserSerializer, serializers
from users.models import User
from recipes.models import Recipe, RecipeIngredient
from ingredients.models import Ingredient
from tags.models import Tag


class UserSerializer(UserSerializer):
    """User Model Serializer."""    
    
    class Meta:
        model = User
        fields = (
            'email', 'id', 'username',
            'first_name', 'last_name')


class IngredientSerializer(serializers.ModelSerializer):
    """Ingredient Model Serializer."""

    class Meta:
        fields = ('id', 'name', 'measurement_unit',)
        model = Ingredient


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """RecipeIngredient Model Serializer."""
    id = serializers.ReadOnlyField(
        source='ingredient.id')
    name = serializers.ReadOnlyField(
        source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit')
    amount = serializers.IntegerField()        
    class Meta:
        model = RecipeIngredient
        fields = ('id', 'name', 'measurement_unit', 'amount')
        

class TagSerializer(serializers.ModelSerializer):
    """Tag Model Serializer."""

    class Meta:
        fields = ('id', 'name', 'color', 'slug',)
        model = Tag


class RecipeReadSerializer(serializers.ModelSerializer):
    """Recipe Model read Serializer."""
    ingredients = RecipeIngredientSerializer(many=True, source='recipe')
    tags = TagSerializer(many=True)
    author = UserSerializer()
    is_favorited = serializers.BooleanField(
        read_only=True)
    class Meta:
        fields = (
            'id',
            'tags',
            'author',
            'ingredients',
            'is_favorited',
            'name',
            'image',
            'text',
            'cooking_time',

        )
        read_only_fields = (
            'id',
            'ingredients',
            'tags',
            'image',
            'name',
            'text',
            'cooking_time',
            'author',
        )
        model = Recipe


class RecipeWriteSerializer(serializers.ModelSerializer):
    """Recipe Model POST и PATCH Serializer."""
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )
    ingredients = IngredientSerializer(many=True)

    class Meta:
        fields = (
            'id',
            'ingredients',
            'tags',
            'image',
            'name',
            'text',
            'cooking_time',
            'author',
        )
        model = Recipe
