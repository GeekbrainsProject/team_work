# Generated by Django 4.1.2 on 2022-10-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlehistory',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]
