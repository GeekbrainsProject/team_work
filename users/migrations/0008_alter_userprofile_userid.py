# Generated by Django 4.1.2 on 2022-11-02 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_options_alter_userprofile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ключ'),
        ),
    ]