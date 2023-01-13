from django.urls import path

from Introduction_To_Django.task.views import home

urlpatterns = [
    path('', home),
]