from django.db import models

# Create your models here.
class libro(models.Model):
    ID = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=50)
    Subtitulo = models.CharField(max_length=50, blank=True)
    FechaPublicacion = models.CharField(max_length=15)
    Editor = models.CharField(max_length=12)
    Descripcion = models.CharField(max_length=1000)
    Imagen = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.Titulo} {self.Subtitulo}"    

class autores(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=15)

class categorias(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=15)

class tablaIntermediaAutores(models.Model):
    ID = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey(libro, on_delete=models.CASCADE)
    id_autor = models.ForeignKey(autores, on_delete=models.CASCADE)

class tablaIntermediaCategorias(models.Model):
    ID = ID = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey(libro, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)