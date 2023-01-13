from django.db import models

# Create your models here.


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering= ('name',)
        abstract=True


class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return f"{self.name}"

class Employees(models.Model):
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        default=''
    )

    egn = models.CharField(
        max_length=10,
        default='',
    )

    image = models.ImageField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.department}"


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )

    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    employees = models.ManyToManyField(
        to=Employees
    )