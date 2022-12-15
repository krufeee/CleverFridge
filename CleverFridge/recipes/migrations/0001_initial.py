# Generated by Django 4.0.5 on 2022-12-08 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeCreateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=30)),
                ('recipe_type', models.CharField(blank=True, choices=[('appetizer', 'appetizer'), ('main dish', 'main dish'), ('dessert', 'dessert')], max_length=10, null=True)),
                ('recipe_cooking_instruction', models.TextField()),
                ('recipe_picture', models.ImageField(blank=True, null=True, upload_to='recipes')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]