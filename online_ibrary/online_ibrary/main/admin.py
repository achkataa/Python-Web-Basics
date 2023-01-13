from django.contrib import admin

# Register your models here.
from online_ibrary.main.models import Profile, Book


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
