from django.shortcuts import render, redirect
from .models import libro
from .models import autores
from .models import categorias
from .models import tablaIntermediaAutores
from .models import tablaIntermediaCategorias
from django.db.models import Q
import threading
from django.http import JsonResponse
import requests
import time

# Create your views here.

def home(request):
    libros = libro.objects.all()
    authors = autores.objects.all()
    categories = categorias.objects.all()

    librosID = libro.objects.values_list('ID')
    interAuthor = tablaIntermediaAutores.objects.all()
    interCate = tablaIntermediaCategorias.objects.all()

    return render(request, "gestion_biblioteca.html", {"libros": libros, "autores":authors, "categorias":categories, "interauthor": interAuthor, "intercate":interCate})

def create(request):
    title = request.POST.get('title')    
    subtitle = request.POST.get('subtitle')
    date = request.POST.get('date')
    editor = request.POST.get('editor')
    desc = request.POST.get('desc')
    authors = request.POST.getlist('author')
    categories = request.POST.getlist('category')

    book = libro.objects.create(Titulo=title, Subtitulo=subtitle, FechaPublicacion=date, Editor=editor, Descripcion=desc)

    for i in range(len(authors)):
        createAuthor(authors[i], book.ID)

    for i in range(len(categories)):
        createCat(categories[i], book.ID)     

    return redirect('/')

def createAuthor(author, bookId):
    interAuthors = tablaIntermediaAutores.objects.create(id_autor_id=author, id_libro_id=bookId)

def createCat(category, bookId):
    interCategory = tablaIntermediaCategorias.objects.create(id_categoria_id =category, id_libro_id=bookId)

def edit(request, id):
    book = libro.objects.get(ID=id)
    authors = autores.objects.all()
    categories = categorias.objects.all()
    #autoresinter = tablaIntermediaAutores.objects.get(id_libro_id=id)
    #categoriasinter = tablaIntermediaCategorias.objects.get(id_libro_id=id)
    return render(
        request, 'edicion_libro.html', 
        {"libro": book, "autores": authors, "categorias": categories}
    )

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
    authors = autores.objects.all()
    categories = categorias.objects.all()
    global result1
    global result2
    result1 = None
    result2 = None
    libros = []

    fisrtDB = threading.Thread(target=consultaGoogle, args=(id, result1))    
    secondDB = threading.Thread(target=consultaOther, args=(id, result2))
    fisrtDB.start()
    secondDB.start()  

    if id:
        booksFound = libro.objects.filter(
            Q(Titulo__icontains = id) |
            Q(Subtitulo__icontains = id) |
            Q(FechaPublicacion__icontains = id) |
            Q(Editor__icontains = id) |
            Q(Descripcion__icontains = id)
        ).distinct()

        if booksFound:
            return render(request, "gestion_biblioteca.html", {"libros": booksFound, "autores":authors, "categorias":categories})
        else:
            #googleList.extend(otherList)
            while result1 is None or result2 is None:
                print(result1)
                print(result2)
                time.sleep(2.5)
            print(result2)
            libros.extend(result1)
            libros.extend(result2)
            return render(request, "gestion_biblioteca.html", {"libros": libros, "autores":authors, "categorias":categories})
    else:
        return render(request, "gestion_biblioteca.html", {"libros": books, "autores":authors, "categorias":categories})
    
def consultaGoogle(id, result):
    url="https://www.googleapis.com/books/v1/volumes?q="+id
    print(url)
    r = requests.get(url)
    answer = r.json()    
    result_list = []

    for i in range(5):
        result_dict = {
            'Titulo':answer['items'][i]['volumeInfo']['title'],
            'Subtitulo':answer['items'][i]['volumeInfo'].get('subtitle'),
            'Descripcion':answer['items'][i]['volumeInfo'].get('description'),
            'categories':answer['items'][i]['volumeInfo'].get('categories'),
            'Editor':answer['items'][i]['volumeInfo'].get('publisher'),
            'FechaPublicacion':answer['items'][i]['volumeInfo'].get('publishedDate'),
            'from':'googleBooks'
        }
        result_list.append(result_dict)

    global result1
    result1 = result_list

def consultaOther(id, result):
    url="https://openlibrary.org/search.json?q="+id
    print(url)
    r = requests.get(url)
    answer = r.json()    
    result_list = []

    for i in range(5): 
        result_dict = {
            'Titulo':answer['docs'][i]['title'],
            'Subtitulo':answer['docs'][i].get('subtitle'),
            'Descripcion':answer['docs'][i].get('first_sentence'),
            'categories':answer['docs'][i].get('subject'),
            'Editor':answer['docs'][i].get('publisher'),
            'FechaPublicacion':answer['docs'][i].get('publish_date'),
            'from': 'Open Library Search'    
        }
        result_list.append(result_dict)

    global result2
    result2 = result_list

def createAutor(request):
    return render(request, 'crear_autor.html')

def createCategory(request):
    return render(request, 'crear_categoria.html')

def registrarAutor(request):
    name = request.POST["name"]
    autor = autores.objects.create(Nombre=name)

    return redirect('../createAuthor/')

def registrarCategoria(request):
    name = request.POST["name"]
    autor = categorias.objects.create(Nombre=name)

    return redirect('../createCategory/')

def getBooks(request):
    id = request.POST["search"]
    books = libro.objects.all()
    global result1
    global result2
    result1 = None
    result2 = None
    libros = []

    fisrtDB = threading.Thread(target=consultaGoogle, args=(id, result1))    
    secondDB = threading.Thread(target=consultaOther, args=(id, result2))
    fisrtDB.start()
    secondDB.start()


    if id:
        booksFound = libro.objects.filter(
            Q(Titulo__icontains = id) |
            Q(Subtitulo__icontains = id) |
            Q(FechaPublicacion__icontains = id) |
            Q(Editor__icontains = id) |
            Q(Descripcion__icontains = id)
        ).distinct()

        if booksFound:
            libros.extend(booksFound)   

        while result1 is None or result2 is None:
                print(result1)
                print(result2)
                time.sleep(2.5)

        libros.extend(result1)
        libros.extend(result2)
        print("return")

        return JsonResponse({'libros':libros})
        
            
    else:
        return books
    
def createBooks(request):
    title = request.POST.get('title')    
    subtitle = request.POST.get('subtitle')
    date = request.POST.get('date')
    editor = request.POST.get('editor')
    desc = request.POST.get('desc')
    authors = request.POST.getlist('author')
    categories = request.POST.getlist('category')


    book = libro.objects.create(Titulo=title, Subtitulo=subtitle, FechaPublicacion=date, Editor=editor, Descripcion=desc)

    return JsonResponse({'libros':book})

def deleteBooks(request, id):
    book = libro.objects.get(ID=id)
    book.delete()

    response = "".join([str(id), " eliminado"])

    return JsonResponse({'libros': response})