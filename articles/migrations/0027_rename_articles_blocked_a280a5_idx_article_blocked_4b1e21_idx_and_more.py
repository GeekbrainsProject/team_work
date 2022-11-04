# Generated by Django 4.1.2 on 2022-11-03 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0026_rename_articles_ar_blocked_286596_idx_articles_blocked_a280a5_idx_and_more'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='article',
            new_name='article_blocked_4b1e21_idx',
            old_name='articles_blocked_a280a5_idx',
        ),
        migrations.RenameIndex(
            model_name='article',
            new_name='article_moderat_5a61d8_idx',
            old_name='articles_moderat_7d6055_idx',
        ),
        migrations.RenameIndex(
            model_name='articlelike',
            new_name='article_lik_dts_1879d3_idx',
            old_name='article_lik_dts_83878c_idx',
        ),
        migrations.RenameIndex(
            model_name='category',
            new_name='category_name_d601b7_idx',
            old_name='categories_name_98d7d5_idx',
        ),
        migrations.RenameIndex(
            model_name='commentlike',
            new_name='comment_lik_dts_6cce61_idx',
            old_name='comment_lik_dts_3dfdb8_idx',
        ),
        migrations.RenameIndex(
            model_name='notification',
            new_name='notificatio_dts_8f1b04_idx',
            old_name='notificatio_dts_b1ccff_idx',
        ),
        migrations.AlterModelTable(
            name='article',
            table='article',
        ),
        migrations.AlterModelTable(
            name='articlecategory',
            table='article_category',
        ),
        migrations.AlterModelTable(
            name='articlelike',
            table='article_like',
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comment',
        ),
        migrations.AlterModelTable(
            name='commentlike',
            table='comment_like',
        ),
        migrations.AlterModelTable(
            name='notification',
            table='notification',
        ),
    ]
