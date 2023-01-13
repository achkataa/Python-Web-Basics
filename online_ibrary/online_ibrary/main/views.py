from django.shortcuts import render, redirect

# Create your views here.
from online_ibrary.main.forms import CreateProfileForm, CreateBookForm, EditProfileForm, DeleteProfileForm
from online_ibrary.main.helpers import get_profile
from online_ibrary.main.models import Book


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create_profile')

    context = {
        'books': Book.objects.all()
    }

    return render(request, 'home-with-profile.html', context)

def add_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateBookForm()

    context = {
        'form': form
    }
    return render(request, 'add-book.html', context)

def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        form = CreateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateBookForm(instance=book)

    context = {
        'form': form,
        'book': book
    }

    return render(request, 'edit-book.html', context)

def book_details(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book
    }

    return render(request, 'book-details.html', context)

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')



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

def profile_page(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)

def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = CreateProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'edit-profile.html', context)

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
        'form': form
    }

    return render(request, 'delete-profile.html', context)