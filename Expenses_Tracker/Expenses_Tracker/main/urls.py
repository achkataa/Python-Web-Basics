from django.urls import path

from Expenses_Tracker.main.views.expense_views import create_expense, edit_expense, delete_expense
from Expenses_Tracker.main.views.generic_views import home_view
from Expenses_Tracker.main.views.profile_views import profile, edit_profile, delete_profile

urlpatterns = [
    path('', home_view, name='home_view'),
    path('create/', create_expense, name='create_expense'),
    path('edit/<int:pk>', edit_expense, name='edit_expense'),
    path('delete/<int:pk>', delete_expense, name='delete_expense'),
    path('profile/', profile, name='profile'),
    path('profiele/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]
