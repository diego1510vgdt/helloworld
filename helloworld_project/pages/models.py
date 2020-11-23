from django.db import models

# Create your models here.

#Modelo del autor
class Autor(models.Model):
    nombre = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.nombre

#Modelo de publicaciones
class Publication(models.Model):
    titulo = models.CharField(max_length = 50)
    contenido = models.CharField(max_length = 250)
    fecha_creacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

#Modelo de comentarios
class Comments(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()
    contenido = models.CharField(max_length = 200)
    idPub = models.ForeignKey(Publication, on_delete=models.CASCADE)
    reccion = models.CharField(max_length = 20)

    def __str__(self):
        return self.contenido