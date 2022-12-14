# Generated by Django 4.0.5 on 2022-12-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0004_alter_ingredientcreatemodel_name'),
        ('recipes', '0002_recipecreatemodel_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipecreatemodel',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipecreatemodel',
            name='ingredients',
            field=models.ManyToManyField(to='ingredients.ingredientcreatemodel'),
        ),
    ]
