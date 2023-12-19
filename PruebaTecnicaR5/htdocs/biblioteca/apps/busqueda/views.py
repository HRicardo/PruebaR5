from django.shortcuts import render, redirect
from .models import libro

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