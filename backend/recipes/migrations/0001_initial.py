# Generated by Django 3.2.16 on 2022-12-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_date', models.DateTimeField(auto_now_add=True, verbose_name='favorite date')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/recipe/', verbose_name='recipe photo')),
                ('name', models.CharField(max_length=200, verbose_name='recipe name')),
                ('text', models.TextField(verbose_name='recipe description')),
                ('cooking_time', models.BigIntegerField(verbose_name='cooking time')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='modifed date')),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='amount')),
            ],
            options={
                'verbose_name': 'ingredient quantity',
                'verbose_name_plural': 'quantity of ingredients',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipes', models.ManyToManyField(related_name='shopping_cart', to='recipes.Recipe', verbose_name='recipe')),
            ],
            options={
                'verbose_name': 'purchase',
                'verbose_name_plural': 'purchases',
                'ordering': ['-id'],
            },
        ),
    ]
