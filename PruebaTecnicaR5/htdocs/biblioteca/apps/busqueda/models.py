from django.db import models

# Create your models here.
class libro(models.Model):
    ID = models.AutoField(primary_key=True) #models.IntegerField(primary_key=True)
    Titulo = models.CharField(max_length=12)
    Subtitulo = models.CharField(max_length=12, blank=True)
    FechaPublicacion = models.DateField()
    Editor = models.CharField(max_length=12)
    Descripcion = models.CharField(max_length=1000)
    Imagen = models.CharField(max_length=50, blank=True)
    autor = models.IntegerField(null=True)
    categoria = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.Titulo} {self.Subtitulo}"
    

class autores(models.Model):
    ID = models.AutoField(primary_key=True) #models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=15)
    Libro_id = models.ForeignKey(libro, on_delete=models.CASCADE)

class categorias(models.Model):
    ID = models.AutoField(primary_key=True) #models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=15)
    Libro_id = models.ForeignKey(libro, on_delete=models.CASCADE)