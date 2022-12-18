from django.db import models
from django.contrib.auth import get_user_model
from tags.models import Tag
from ingredients.models import Ingredient


User = get_user_model()

class Recipe(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='ingredients',
        related_name='recipe',
#        on_delete=models.PROTECT,
        )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='tags',
        related_name='recipe',
        blank=True,)
    image = models.ImageField(
        'recipe photo',
        upload_to='static/recipe/',
        blank=True,
        null=True)
    name = models.CharField(
        'recipe name',
        max_length=200)
    text = models.TextField(
        'recipe description',
        blank=False)
    cooking_time = models.BigIntegerField(
        'cooking time')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='author')
    pub_date = models.DateTimeField(
        'creation date',
        auto_now_add=True)
    date_update = models.DateTimeField(
        'modifed date',
        auto_now=True)

    def get_ingredients(self):
        ingredients = [ingredient['name'] for ingredient in self.ingredients.values('name')]
        return ingredients

    def get_tags(self):
        tags = [tag['name'] for tag in self.tags.values('name')]
        return tags        



    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ('-pub_date', )        

    def __str__(self) -> str:
        return f'{self.name} from {self.author.first_name}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe')
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient')
    amount = models.PositiveSmallIntegerField(
        'amount',)

    class Meta:
        verbose_name = 'ingredient quantity'
        verbose_name_plural = 'quantity of ingredients'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique ingredient')]


class FavoriteRecipe(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_recipe',
        verbose_name='user',
    )
    recipes = models.ManyToManyField(
        Recipe,
        related_name='favorite_recipe',
        verbose_name='recipe',
    )
    favorite_date = models.DateTimeField(
        'favorite date',
        auto_now_add=True)

    def get_recipe(self):
        shopping_cart = [recipe['name'] for recipe in self.recipes.values('name')]
        return shopping_cart

    # class Meta:
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['user', 'recipe'], name='unique_favorite')
        # ]

    def __str__(self):
        return f'{self.user} favorite {self.recipes}'


class ShoppingCart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='user')
    recipes = models.ManyToManyField(
        Recipe,
        related_name='shopping_cart',
        verbose_name='recipe')

    class Meta:
        verbose_name = 'purchase'
        verbose_name_plural = 'purchases'
        ordering = ['-id']

    def get_recipe(self):
        shopping_cart = [recipe['name'] for recipe in self.recipes.values('name')]
        return shopping_cart

    def __str__(self):
        shopping_cart = [recipe['name'] for recipe in self.recipes.values('name')]
        return f'{self.user} shopping cart: {shopping_cart}'