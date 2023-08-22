from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField()


class Album(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_salida = models.DateField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, null=True)

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    
class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.SET_DEFAULT, default=None)
    generos = models.ManyToManyField(Genero)

class AlbumArte(models.Model):
    imagen = models.ImageField(upload_to="album_cover/", default='album_cover/batman.jpg')
    descripcion = models.TextField(max_length=500, default=None)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)


class Archivo(models.Model):
    archivo = models.FileField(upload_to='descargas/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    nombre = models.CharField(max_length=50)
    votos =  models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.nombre
    


