# Generated by Django 4.0.2 on 2022-02-20 15:53

import Expenses_Tracker.main.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[Expenses_Tracker.main.validators.MaxFileSizeInMbValidator(5)]),
        ),
    ]
