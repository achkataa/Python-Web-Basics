from django.shortcuts import render, redirect

from Expenses_Tracker.main.forms.profile_forms import CreateProfileForm
from Expenses_Tracker.main.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def get_total_money_left():
    profile = get_profile()
    if profile:
        expenses = Expense.objects.all()
        total_expenses = sum([expense.price for expense in expenses])
        return profile.budget - total_expenses


def home_view(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    if profile:
        template = 'main_templates/home-with-profile.html'
    else:
        template = 'main_templates/home-no-profile.html'

    if request.method == "POST":
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_view')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'expenses': expenses,
        'profile': profile,
        'budget_left': get_total_money_left()
    }

    return render(request, template, context)