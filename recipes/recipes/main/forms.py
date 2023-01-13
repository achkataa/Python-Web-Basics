from django import forms

from recipes.main.helpers import DisableFieldsMixin
from recipes.main.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image', 'description', 'ingredients', 'time')

    # def clean(self):
    #     super(CreateRecipeForm, self).clean()
    #
    #     ingredients = self.cleaned_data.get('ingredients')
    #
    #     if len(ingredients) < 5:
    #         self._errors['ingredients'] = self.error_class([
    #             'The ingredients should be separated by comma'])
    #
    #     return self.cleaned_data

class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class DeleteRecipeForm(forms.ModelForm, DisableFieldsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disable_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = ('title', 'image', 'description', 'ingredients', 'time')