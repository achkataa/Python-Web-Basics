from django import forms

from online_ibrary.main.helpers import DisabledFieldsMixin
from online_ibrary.main.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'image': forms.URLInput(attrs={'placeholder': 'URL'})
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class DeleteProfileForm(forms.ModelForm, DisabledFieldsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disable_fields()

    def save(self, commit=True):
        Book.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'FIction, Novel, Crime...'})
        }

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'