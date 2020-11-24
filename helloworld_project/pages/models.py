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
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    reccion = models.IntegerField(default = 0)

    def __str__(self):
        return self.titulo

#Modelo de comentarios
class Comment(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    contenido = models.CharField(max_length = 200)

    def __str__(self):
        return self.contenido