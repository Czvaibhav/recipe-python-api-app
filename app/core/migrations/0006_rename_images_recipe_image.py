# Generated by Django 3.2.24 on 2024-02-14 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recipe_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='images',
            new_name='image',
        ),
    ]
