# Generated by Django 3.1.7 on 2021-02-26 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210220_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeding',
            old_name='cat',
            new_name='dog',
        ),
    ]
