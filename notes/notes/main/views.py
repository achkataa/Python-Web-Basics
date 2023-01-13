from django.shortcuts import render, redirect

# Create your views here.
from notes.main.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm, DeleteProfileForm
from notes.main.helpers import get_profile
from notes.main.models import Note


def home_page(request):
    # profile = get_profile()
    # notes = Note.objects.all()
    # if not profile:
    #     return redirect('create_profile')
    #
    # context = {
    #     'notes': notes
    # }

    return render(request, 'home-with-profile.html')

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

    return render(request, 'home-no-profile.html', context)

def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateNoteForm()

    context = {
        'form': form
    }

    return render(request, 'note-create.html', context)

def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)

def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)

def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)

def profile(request):
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
        'notes_count': Note.objects.count()
    }

    return render(request, 'profile.html', context)
