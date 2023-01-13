from django.shortcuts import render, redirect

from Expenses_Tracker.main.forms.expense_forms import CreateExpenseForm, EditExpenseForm, DeleteExpenseForm
from Expenses_Tracker.main.models import Expense


def expense_action(request, model_form, instance, redirect_url, template):
    if request.method == "POST":
        form = model_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = model_form(instance=instance)

    context = {
        'form': form,
        'expense': instance
    }

    return render(request, template, context)


def create_expense(request):
    return expense_action(request, CreateExpenseForm, Expense(), 'home_view', 'main_templates/expense-create.html')

def edit_expense(request, pk):
    return expense_action(request, EditExpenseForm, Expense.objects.get(pk=pk), 'home_view', 'main_templates/expense-edit.html')

def delete_expense(request, pk):
    return expense_action(request, DeleteExpenseForm, Expense.objects.get(pk=pk), 'home_view', 'main_templates/expense-delete.html')

