from django.urls import path

from employees_app.employees.views import HomeView, create_employee, edit_employee

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', create_employee, name='create_employee'),
    path('edit/<int:pk>/', edit_employee, name='edit_employee'),

]