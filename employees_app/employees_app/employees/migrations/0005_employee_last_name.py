# Generated by Django 4.0.1 on 2022-02-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='', editable=False, max_length=40),
        ),
    ]
