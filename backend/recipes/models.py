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
        related_name='recipes',
#        on_delete=models.PROTECT,
        null=True)
    tags = models.ManyToManyField(
        Tag,
        verbose_name='tags',
        related_name='recipes',
        null=True)
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
        related_name='recipes',
        verbose_name='author')
    pub_date = models.DateTimeField(
        'creation date',
        auto_now_add=True)
    date_update = models.DateTimeField(
        'modifed date',
        auto_now=True)


    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ('-pub_date', )        

    def __str__(self) -> str:
        return f'{self.name} from {self.author.first_name}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,)
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





