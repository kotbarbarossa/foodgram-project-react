

from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    email = models.EmailField(
        'email',
        max_length=200,
        unique=True,)
    first_name = models.CharField(
        'name',
        max_length=150)
    last_name = models.CharField(
        'surname',
        max_length=150)
    text = models.TextField()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('id',)

    def __str__(self):
        return self.email


class Subscribe(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='subscribe_user',
        verbose_name='follower',
    )
    authors = models.ManyToManyField(
        User,
        related_name='subscribe_author',
        verbose_name='author',
    )
    subscribe_date = models.DateTimeField(
        'subscribe date',
        auto_now_add=True)    

    def get_author(self):
        shopping_cart = [author['email'] for author in self.authors.values('email')]
        return shopping_cart

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['user', 'authors'], name='unique_follow')
    #     ]

    def __str__(self):
        return f'{self.user} subscibed to {self.authors}'
