# Generated by Django 4.2.8 on 2023-12-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_emailmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]