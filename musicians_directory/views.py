from django.shortcuts import get_object_or_404, render, redirect
from musician import form as mform, models as mmodels  
from album import form as aform, models as amodels  

def Home(request):
    mdata =  mmodels.Musician.objects.all()
    adata =  amodels.Album.objects.all()
    return render(request, 'index.html', {'mdata': mdata, 'adata': adata})

def addmusician(request):
    if request.method == 'POST':
        form = mform.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'addmusician.html', {'mform': form})
    else:
        form =  mform.MusicianForm()
        return render(request, 'addmusician.html', {'mform': form})

def addalbum(request):
    if request.method == 'POST':
        form = aform.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'addalbum.html', {'aform': form})
    else:
        form =  aform.AlbumForm()
        return render(request, 'addalbum.html', {'aform': form})


def updatemusician(request):
    email = request.GET.get('email')
    musician = get_object_or_404(mmodels.Musician, email=email)

    if request.method == 'POST':
        musician.email = request.POST.get('email', musician.email)
        musician.phone_number = request.POST.get('phone_number', musician.phone_number)
        musician.instrument_type = request.POST.get('instrument_type', musician.instrument_type)
        musician.save()
        return redirect('home')

    else:
        return render(request, 'updatemusician.html', {'musician': musician})

def updatealbum(request):
    name = request.GET.get('name')
    album = get_object_or_404(amodels.Album, name=name)

    if request.method == 'POST':
        album.name = request.POST.get('name', album.name)
        album.release_date = request.POST.get('release_date', album.release_date)
        album.rating = request.POST.get('rating', album.rating)
        album.save()
        return redirect('home')
    else:
        release_date = album.release_date.strftime('%Y-%m-%d')
        return render(request, 'updatealbum.html', {'album': album,  'release_date': release_date})

def deletealbum(request):
    name = request.GET.get('name')
    album = get_object_or_404(amodels.Album, name=name)
    album.delete()
    return redirect('home')


def deletemusician(request):
    email = request.GET.get('email')
    musician = get_object_or_404(mmodels.Musician, email=email)
    musician.delete()
    return redirect('home')
