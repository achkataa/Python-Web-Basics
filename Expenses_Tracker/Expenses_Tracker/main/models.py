from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.
from Expenses_Tracker.main.validators import only_letters_validator, MaxFileSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2
    BUDGET_MIN_VALUE = 0
    IMAGE_MAX_SIZE_IN_MB = 5

    first_name = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    budget = models.FloatField(
        default=0,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        )

    )

    profile_image = models.ImageField(
        null=True,
        blank=True,
        validators= (
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )


class Expense(models.Model):
    title = models.CharField(
        max_length=30
    )

    expense_image = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()
