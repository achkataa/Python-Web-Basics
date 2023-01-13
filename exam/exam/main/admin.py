from django.contrib import admin

# Register your models here.
from exam.main.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name',)