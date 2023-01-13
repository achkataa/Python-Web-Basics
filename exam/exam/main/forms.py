from django import forms

from exam.main.helpers import DisableFieldsMixin
from exam.main.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age'}),
        }

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image', 'price')

        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.TextInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price'}),
        }

class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class DeleteAlbumForm(forms.ModelForm, DisableFieldsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disable_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        Album.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()

