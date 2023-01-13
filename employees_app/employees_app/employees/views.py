from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from employees_app.employees.models import Employees, Department

def is_age_positive(value):
    if not value >= 0:
        raise ValidationError('Age must be a positive number')


from django import forms

# class EmployeesForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#     )
#
#     last_name = forms.CharField(
#         max_length=30,
#         required=True,
#     )
#
#     age = forms.IntegerField(
#         required=True,
#         validators=(
#             is_age_positive,
#         )
#     )


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'custom-select'}),
            'egn': forms.TextInput(attrs={'class': 'form-control'}),


        }

class EditEmployeeForm(EmployeesForm):
    class Meta:
        model = Employees
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(attrs={'readonly': 'readonly'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'custom-select'}),
        }

class OrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First Name'),
            ('last_name', 'Last Name'),
        ),


    )


# from django.views.generic import TemplateView
from django.views import generic
# def home_view(request):
#     return render(request, 'home.html')

class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Template class-based view'
        return context




def create_employee(request):
    if request.method == "POST":
        employee_form = EmployeesForm(request.POST, request.FILES)
        if employee_form.is_valid():
            employee_form.save()
    else:
        employee_form = EmployeesForm()

    employee_order_form = OrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order by', 'first_name')
    context = {
        'employee_form': employee_form,
        'employees': Employees.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }

    return render(request, 'create_employee.html', context)

def edit_employee(request, pk):
    employee = Employees.objects.get(pk=pk)
    if request.method == 'POST':
        employee_form = EditEmployeeForm(request.POST, request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create_employee')
    else:
        employee_form = EditEmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form
    }

    return render(request, 'edit.html', context)