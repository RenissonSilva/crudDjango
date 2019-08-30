from django.shortcuts import render, redirect
from .models import Manga
from .forms import MangaForm


def list_mangas(request):
    mangas = Manga.objects.all()
    return render(request, 'mangas.html', {'mangas': mangas})


def create_manga(request):
    form = MangaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_mangas')

    return render(request, 'mangas-form.html', {'form': form})


def update_manga(request, id):
    manga = Manga.objects.get(id=id)
    form = MangaForm(request.POST or None, instance=manga)

    if form.is_valid():
        form.save()
        return redirect('list_mangas')

    return render(request, 'mangas-form.html', {'form': form, 'manga': manga})


def delete_manga(request, id):
    manga = Manga.objects.get(id=id)

    if request.method == 'POST':
        manga.delete()
        return redirect('list_mangas')

    return render(request, 'prod-delete-confirm.html', {'manga': manga})
