from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarLibro/', views.create),
    path('editarLibro/<id>', views.edit),
    path('actualizarLibro/', views.update),
    path("eliminarLibro/<id>", views.delete),
    path("search/", views.search),
    path("createAuthor/", views.createAutor),
    path("createCategory/", views.createCategory),
    path("registerAuthor/", views.registrarAutor),
    path("registerCategory/", views.registrarCategoria),
    path("getBookspost/", views.getBooks),
    path("createBookspost/", views.createBooks),
    path("deleteBookspost/<id>", views.deleteBooks)
]