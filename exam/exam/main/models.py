from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.
from exam.main.validators import only_letters_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(0),
        )
    )

class Album(models.Model):
    PopMusic = 'Pop Music'
    JazzMusic = 'Jazz Music'
    RBMusic = 'R&B Music'
    RockMusic = 'Rock Music'
    CountryMusic = 'Country Music'
    DanceMusic = 'Dance Music'
    HipHopMusic = 'Hip Hop Music'
    Other = 'Other'

    GENRES = [(x, x) for x in (PopMusic, JazzMusic, RBMusic, RockMusic, CountryMusic, DanceMusic, HipHopMusic, Other)]

    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30
    )

    genre = models.CharField(
        max_length=30,
        choices=GENRES
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        )
    )

