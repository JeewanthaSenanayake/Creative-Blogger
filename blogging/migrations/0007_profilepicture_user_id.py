# Generated by Django 4.2.11 on 2024-04-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0006_rename_profilepic_profilepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepicture',
            name='user_id',
            field=models.TextField(default='0'),
        ),
    ]