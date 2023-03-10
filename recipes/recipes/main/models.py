from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(
        max_length=30
    )

    image = models.URLField(
        verbose_name='Image URL'
    )

    description = models.TextField()

    ingredients = models.CharField(
        max_length=250
    )

    time = models.IntegerField(
        verbose_name='Time (Minutes)'
    )
