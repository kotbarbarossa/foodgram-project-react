from django.db import models
from django.utils.html import format_html
from django.contrib import admin


class Tag(models.Model):
    """
        Tag model.
        COLOR_EXAMPLES = [
            ('#FF0000', 'RED'),
            ('#FF8000', 'ORANGE'),
            ('#FFFF00', 'YELLOW'),
            ('#80FF00', 'GREEN'),
            ('#00FFFF', 'LIGHT_BLUE'),
            ('#0080FF', 'BLUE'),
            ('#7F00FF', 'EPIC'),
            ('#FF00FF', 'PINK'),
            ('#FF007F', 'CORAL'),
        ]
    """

    name = models.CharField(
        'tag name',
        max_length=60,
        unique=True)
    color = models.CharField(
        'HEX tag color',
        max_length=7,
        unique=True)
    slug = models.SlugField(
        'link',
        max_length=100,
        unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['-id']

    def __str__(self):
        return self.name

    @admin.display(ordering='name')
    def colored_color(self):
        return format_html(
            f'<span style="color: {self.color};">{self.color}</span>'
        )
