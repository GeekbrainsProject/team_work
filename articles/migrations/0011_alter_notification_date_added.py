# Generated by Django 4.1.2 on 2022-10-20 09:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0010_rename_like_articlelike_commentlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date_added',
            field=models.DateField(db_column='dts', default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]
