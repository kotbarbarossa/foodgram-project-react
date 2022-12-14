from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        'ingredient name',
        max_length=200,
        unique=True)
    measurement_unit = models.CharField(
        'measurement unit',
        max_length=200)


    class Meta:
        ordering = ['name']
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self) -> str:
        return self.name
