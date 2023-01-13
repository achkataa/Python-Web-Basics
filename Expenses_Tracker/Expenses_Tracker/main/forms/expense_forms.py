from django import forms

from Expenses_Tracker.main.models import Expense


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

class DeleteExpenseForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'readonly'}),
            'expense_image': forms.URLInput(attrs={'readonly': 'readonly'}),
            'description': forms.Textarea(attrs={'readonly': 'readonly'}),
            'price': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }


