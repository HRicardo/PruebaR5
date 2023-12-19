from django.shortcuts import render, redirect
from .models import libro
from django.db.models import Q
import requests
import logging

# Create your views here.

def home(request):
    libros = libro.objects.all()
    return render(request, "gestion_biblioteca.html", {"libros": libros})

def create(request):
    title = request.POST['title']
    subtitle = request.POST['subtitle']
    date = request.POST['date']
    editor = request.POST['editor']
    desc = request.POST['desc']

    book = libro.objects.create(Titulo=title, Subtitulo=subtitle, FechaPublicacion=date, Editor=editor, Descripcion=desc, autor=1, categoria=1)

    return redirect('/')

def edit(request, id):
    book = libro.objects.get(ID=id)
    return render(request, 'edicion_libro.html', {"libro": book})

def delete(request, id):
    book = libro.objects.get(ID=id)
    book.delete()

    return redirect('/')

def update(request):
    id = request.POST['id']
    title = request.POST['title']
    subtitle = request.POST['subtitle']
    date = request.POST['date']
    editor = request.POST['editor']
    desc = request.POST['desc']

    book = libro.objects.get(ID=id)

    book.Titulo = title
    book.Subtitulo = subtitle
    book.FechaPublicacion = date
    book.Editor = editor
    book.Descripcion = desc

    book.save()

    return redirect("/")

def search(request):
    id = request.POST["search"]
    books = libro.objects.all()
    logger = logging.getLogger("mylogger")
    logger.info("Whatever to log")

    googleList = consultaGoogle(id)

    if id:
        booksFound = libro.objects.filter(
            Q(Titulo__icontains = id) |
            Q(Subtitulo__icontains = id) |
            Q(FechaPublicacion__icontains = id) |
            Q(Editor__icontains = id) |
            Q(Descripcion__icontains = id)
        ).distinct()

        return render(request, "gestion_biblioteca.html", {"libros": booksFound})
    else:
        return render(request, "gestion_biblioteca.html", {"libros": googleList})
    
async def consultaGoogle(id):
    url="https://www.googleapis.com/books/v1/volumes?q="+id
    print(url)
    r = requests.get(url)
    answer = await r.json()
    result_list = []
    for i in range(10):
        result_dict = {
            'Titulo':answer['items'][i]['volumeInfo']['title'],
            'Subtitulo':answer['items'][i]['volumeInfo'].get('subtitle'),
            'Descripcion':answer['items'][i]['volumeInfo'].get('description'),
            'categories':answer['items'][i]['volumeInfo'].get('categories'),
            'Editor':answer['items'][i]['volumeInfo'].get('publisher'),
            'FechaPublicacion':answer['items'][i]['volumeInfo'].get('publishedDate')         
        }
        result_list.append(result_dict)
    return result_list