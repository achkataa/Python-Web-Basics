from django.shortcuts import render, redirect

# Create your views here.
from exam.main.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from exam.main.helpers import get_profile
from exam.main.models import Album


def home(request):
    albums = Album.objects.all()
    profile = get_profile()
    if not profile:
        return redirect('create_profile')

    context = {
        'albums': albums
    }

    return render(request, 'templates/home-with-profile.html', context)

def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }

    return render(request, 'templates/home-no-profile.html', context)

def add_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form
    }
    return render(request, 'templates/add-album.html', context)

def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }

    return render(request, 'templates/album-details.html', context)

def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'templates/edit-album.html', context)

def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'templates/delete-album.html', context)

def profile_details(request):
    profile = get_profile()

    context = {
        'profile': profile,
        'total_albums': Album.objects.count(),
    }

    return render(request, 'templates/profile-details.html', context)

def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'templates/profile-delete.html', context)