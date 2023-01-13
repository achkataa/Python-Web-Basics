import os

from django import forms

from Expenses_Tracker.main.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')

        widgets = {
            'profile_image': forms.FileInput(attrs={'class': 'form-file'})
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):\

    def save(self, commit=True):
        Expense.objects.all().delete()
        image_path = self.instance.profile_image.path
        self.instance.delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


