# Generated by Django 4.0.5 on 2022-12-13 12:21

import CleverFridge.core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(5), CleverFridge.core.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(5), CleverFridge.core.validators.validate_only_letters]),
        ),
    ]
