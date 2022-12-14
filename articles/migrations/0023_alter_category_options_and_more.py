# Generated by Django 4.1.2 on 2022-11-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0022_alter_article_options_alter_articlecategory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['blocked'], name='articles_ar_blocked_286596_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['moderation'], name='articles_ar_moderat_f293b2_idx'),
        ),
        migrations.AddIndex(
            model_name='articlehistory',
            index=models.Index(fields=['change_type'], name='articles_ar_change__541634_idx'),
        ),
        migrations.AddIndex(
            model_name='articlelike',
            index=models.Index(fields=['date_added'], name='articles_ar_dts_d3ee4e_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='articles_ca_name_b48539_idx'),
        ),
        migrations.AddIndex(
            model_name='commentlike',
            index=models.Index(fields=['date_added'], name='articles_co_dts_f3536f_idx'),
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['date_added'], name='articles_no_dts_decc32_idx'),
        ),
    ]
