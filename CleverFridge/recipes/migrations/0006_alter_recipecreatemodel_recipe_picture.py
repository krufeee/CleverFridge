# Generated by Django 4.0.5 on 2022-12-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipecreatemodel_recipe_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipecreatemodel',
            name='recipe_picture',
            field=models.ImageField(blank=True, default='NoPictureForRecipe.jpg', null=True, upload_to='recipes'),
        ),
    ]
