from django.db import models
from datetime import datetime
from taller.settings import MEDIA_URL,STATIC_URL
from nucleo.user.models import User


class Coche(models.Model):
    Marca = models.CharField(max_length=50, verbose_name='Marca')
    Modelo = models.CharField(max_length=50, verbose_name='Modelo')
    Color = models.CharField(max_length=50, verbose_name='Color')
    FechaMatri = models.DateField(verbose_name='Fecha de matriculacion')
    Imagen = models.ImageField(upload_to='coche/', null=True, blank=True)
    Cliente_id= models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Cliente')

    def __str__(self):
        return self.Marca+" "+self.Modelo
    
    def get_imagen(self):
        if self.Imagen:
            return '{}{}'.format(MEDIA_URL ,self.Imagen)
        return '{}{}'.format(STATIC_URL,'img/vacio.png')

    class Meta:
        verbose_name ='Coche'
        verbose_name_plural= 'Coches'
        db_table='coche'
        ordering = ['id']

   
class Noticia(models.Model):
    Titulo = models.CharField(max_length=100, verbose_name='Titulo')
    Texto = models.CharField(max_length=500, verbose_name='Texto')
    Foto = models.ImageField(upload_to='noticia/', null=True, blank=True)
    FechaCreacion = models.DateTimeField(auto_now_add=True)
    FechaModi = models.DateTimeField(auto_now=True)
    Id_Mecanico = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Mecanico')

    def __str__(self):
        return self.Titulo
    
    def get_imagen(self):
        if self.Foto:
            return '{}{}'.format(MEDIA_URL ,self.Foto)
        return '{}{}'.format(STATIC_URL,'img/vacio.png')

    class Meta:
        verbose_name ='Noticia'
        verbose_name_plural= 'Noticias'
        db_table='noticia'
        ordering = ['id']


class Reparacion(models.Model):
    FechaSolicitud = models.DateTimeField(auto_now=True)
    FechaArreglo= models.DateField(auto_now_add=True)
    Motivo = models.CharField(max_length=500, verbose_name='Motivo')
    Observacion = models.CharField(max_length=500, verbose_name='Observacion')
    Id_Coche = models.ForeignKey(Coche, on_delete=models.CASCADE,  verbose_name='Coche')
    Id_Cliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cliente')
    Id_Mecanico= models.ManyToManyField(User,related_name='Mecanicos',verbose_name='Mecanicos')
    Arreglado = models.BooleanField(default=False)
    Pendiente = models.BooleanField(default=True)


    def __str__(self):
        return self.Motivo
    
    class Meta:
        verbose_name ='Reparacion'
        verbose_name_plural= 'Reparaciones'
        db_table='reparacion'
        ordering = ['id']
    
    def clean(self):
        cleaned= super().clean()
        return cleaned


