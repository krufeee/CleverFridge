# Generated by Django 4.0.5 on 2022-12-17 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_recipecreatemodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipecreatemodel',
            name='recipe_type',
            field=models.CharField(blank=True, choices=[('appetizer', 'appetizer'), ('main dish', 'main dish'), ('dessert', 'dessert'), ('salad', 'salad')], max_length=10, null=True),
        ),
    ]