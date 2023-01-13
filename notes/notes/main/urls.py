from django.urls import path

from notes.main.views import home_page, add_note, edit_note, delete_note, note_details, profile, create_profile

urlpatterns = [
    path('', home_page, name='home'),
    path('create', create_profile, name='create_profile'),
    path('add/', add_note, name='add_note'),
    path('edit/<int:pk>/', edit_note, name='edit_note'),
    path('delete/<int:pk>/', delete_note, name='delete_note'),
    path('details/<int:pk>/', note_details, name='note_details'),
    path('profile/', profile, name='profile'),


]