from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from CleverFridge.core.validators import validate_only_letters



class AppUser(AbstractUser):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    GENDERS = (
        (MALE, MALE),
        (FEMALE, FEMALE),
        (OTHER, OTHER)
    )
    MIN_LEN_FIRST_NAME = 5
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 5
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDERS,
    )

