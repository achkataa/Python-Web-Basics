from django.contrib import admin


from Introduction_To_Django.task.models import Task


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    pass
