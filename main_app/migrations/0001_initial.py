# Generated by Django 3.1.6 on 2021-02-16 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('breed', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=150)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
