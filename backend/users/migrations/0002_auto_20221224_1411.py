# Generated by Django 3.2.16 on 2022-12-24 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribe',
            options={'verbose_name': 'subscribe', 'verbose_name_plural': 'subscriptions'},
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='authors',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='subscribe_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='subscribe date'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='follower'),
        ),
        migrations.AddConstraint(
            model_name='subscribe',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='unique_subscription'),
        ),
    ]
