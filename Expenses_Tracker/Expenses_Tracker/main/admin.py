from django.contrib import admin

# Register your models here.
from Expenses_Tracker.main.models import Profile, Expense


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title',)
