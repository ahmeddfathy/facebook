# Generated by Django 4.2.1 on 2023-05-22 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Car',
            new_name='Login',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='username',
        ),
    ]
