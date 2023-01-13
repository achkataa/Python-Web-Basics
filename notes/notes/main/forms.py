from django import forms

from notes.main.helpers import DisableFieldsMixin
from notes.main.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        Note.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class DeleteNoteForm(forms.ModelForm, DisableFieldsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disable_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = '__all__'

