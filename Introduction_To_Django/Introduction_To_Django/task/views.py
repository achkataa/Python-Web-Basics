from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Introduction_To_Django.task.models import Task


# def home(request):
#     tasks = Task.objects.all()
#     item_strings = [f'<li>{t.title}</li>' for t in tasks]
#     string = ''.join(item_strings)
#
#     return HttpResponse(string)


def home(request):
    context = {
        'title': 'it works from view',
        'tasks': Task.objects.all()
    }
    return render(request, 'home.html', context)
