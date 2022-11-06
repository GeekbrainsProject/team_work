# Generated by Django 4.1.2 on 2022-11-06 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_delete_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]