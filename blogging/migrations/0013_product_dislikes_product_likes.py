# Generated by Django 4.2.11 on 2024-05-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0012_product_userid_alter_profileimage_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
