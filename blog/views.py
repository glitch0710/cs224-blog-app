from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Album, Song
from .forms import SongForm
from django.contrib import messages

# Create your views here.
def index(request):
    name = "Rhogiel Andoy"
    subjects = ["CS224", "CS221", "CS225", "CS214"]
    age = None

    if request.method == "POST":
        age = int(request.POST.get('age', 0))

    context = {
        'age': age,
        'name': name,
        'subjects': subjects,
    }

    return render(request, 'index.html', context)


def another_page(request):
    song_form = SongForm()
    if request.method == 'GET':

        data = request.GET.get('search_song')

        if data:
            songs = Song.objects.filter(name__icontains=data)
        else:
            songs = Song.objects.all()

        context = {
            'form': song_form,
            'songs': songs,
        }

        return render(request, 'pagetwo.html', context)
    else:
        new_song = SongForm(data=request.POST)

        if new_song.is_valid():
            new_song.save()

        messages.success(request, "New song has been added.")
        return redirect('another_page')


def another_page_one(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Exception:
        messages.error(request, "Song not found")
        return redirect('another_page')

    if request.method == 'GET':
        form = SongForm(instance=song)

        context = {
            'form': form,
        }

        return render(request, 'pagefour.html', context)

    else:
        updated_song = SongForm(data=request.POST, instance=song)

        if updated_song.is_valid():
            updated_song.save()

            messages.success(request, "Song has been updated")
            return redirect('another_page')
        else:
            messages.error(request, "Error upon saving. Please try again.")
            return redirect('another_page')
        

def delete_song(request, pk):
    if request.method == 'GET':
        try:
            song = Song.objects.get(pk=pk)

            song.delete()

            messages.success(request, "Song has been deleted.")
            return redirect('another_page')
        except Exception:
            messages.error(request, "Song not found")
            return redirect('another_page')


def page_three(request):
    if request.method == 'GET':
        return render(request, 'pagethree.html')
    else:
        try:
            data = request.POST

            title = data.get('title')
            artist = data.get('artist')
            genre = data.get('genre')

            new_album = Album(title=title, artist=artist, genre=genre)
            new_album.save()

            messages.success(request, "New album has been added.")
            return redirect('page_three')
        except Exception:
            messages.error(request, "Saving encountered an error. Please try again later.")
            return redirect('page_three')
