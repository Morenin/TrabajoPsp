from django.contrib import admin
from nucleo.models import Coche,Noticia,Reparacion

# Register your models here.
class CocheAdmin(admin.ModelAdmin):
    list_display = ['Marca','Modelo','Color','Cliente_id','FechaMatri']
    search_fields=['Marca']

admin.site.register(Coche,CocheAdmin)
admin.site.register(Noticia)
admin.site.register(Reparacion)