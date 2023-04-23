# Generated by Django 4.1.5 on 2023-03-30 12:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0004_alter_status_profile_picture_alter_status_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
