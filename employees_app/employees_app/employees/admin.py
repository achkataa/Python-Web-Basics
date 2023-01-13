from django.contrib import admin

# Register your models here.
from employees_app.employees.models import Employees, Department


#
@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'department')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on', 'last_updated_on')
