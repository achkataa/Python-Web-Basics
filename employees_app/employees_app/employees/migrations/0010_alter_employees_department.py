# Generated by Django 4.0.1 on 2022-02-02 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_employees_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='employees.department'),
        ),
    ]
