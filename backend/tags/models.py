from django.db import models


class Tag(models.Model):
    name = models.CharField(
        'tag name',
        max_length=60,
        unique=True)
    color = models.CharField(
        'tag color',
        max_length=10,
        unique=True
        )
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
