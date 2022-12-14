# Generated by Django 4.1.2 on 2022-10-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0016_alter_notification_options_notification_article_uid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-creation_date']},
        ),
        migrations.AlterField(
            model_name='article',
            name='creation_date',
            field=models.DateField(auto_now_add=True, db_column='creation_date', db_index=True),
        ),
    ]
