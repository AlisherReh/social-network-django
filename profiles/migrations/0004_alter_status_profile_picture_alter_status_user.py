# Generated by Django 4.1.5 on 2023-03-21 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_status_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='profile_picture',
            field=models.ImageField(blank=True, default='123_fvipp2r.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='status',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
