from django.contrib import admin

# Register your models here.
from notes.main.models import Profile, Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title',)
