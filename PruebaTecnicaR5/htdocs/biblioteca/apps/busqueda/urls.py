from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarLibro/', views.create),
    path('editarLibro/<id>', views.edit),
    path('actualizarLibro/', views.update),
    path("eliminarLibro/<id>", views.delete)
]