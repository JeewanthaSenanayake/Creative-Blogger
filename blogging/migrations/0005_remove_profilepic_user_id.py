# Generated by Django 4.2.11 on 2024-04-30 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0004_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepic',
            name='user_id',
        ),
    ]
