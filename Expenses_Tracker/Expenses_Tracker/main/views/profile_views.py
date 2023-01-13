from django.shortcuts import render, redirect

from Expenses_Tracker.main.forms.profile_forms import EditProfileForm, DeleteProfileForm
from Expenses_Tracker.main.models import Expense
from Expenses_Tracker.main.views.generic_views import get_profile, get_total_money_left


def profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
        'total_items': len(list(Expense.objects.all())),
        'left_budget': get_total_money_left()
    }
    return render(request, 'main_templates/profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'main_templates/profile-edit.html', context)

def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home_view')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'main_templates/profile-delete.html', context)