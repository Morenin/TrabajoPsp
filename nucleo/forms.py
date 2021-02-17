from django.forms import *
from nucleo.models import Coche, Noticia, Reparacion


class CocheForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']='form-control'
            form.field.widget.attrs['autocomplete']='off'
        self.fields['Marca'].widget.attrs['autofocus']=True
    class Meta:
        model=Coche
        fields='__all__'
        widgets = {
            'FechaMatri': TextInput(attrs={'type':'date'})
        }

        exclude ={'Cliente_id'} 
        
    

class NoticiaForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']='form-control'
            form.field.widget.attrs['autocomplete']='off'
        self.fields['Titulo'].widget.attrs['autofocus']=True
    class Meta:
        model=Noticia
        fields='__all__'
        widgets = {
            'FechaCreacion': TextInput(attrs={'type':'date'}),
            'FechaModi': TextInput(attrs={'type':'date'})
            
        }

        exclude ={'Id_Mecanico'} 

class ReparacionForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']='form-control'
            form.field.widget.attrs['autocomplete']='off'
        self.fields['Motivo'].widget.attrs['autofocus']=True
        
    class Meta:
        model=Reparacion
        fields='__all__'
        widgets = {
            'FechaArreglo': TextInput(attrs={'type':'date'}),
            'Id_Mecanico': Select(attrs={'style':'width 100%'})
        }
        exclude ={'Pendiente','Id_Cliente'} 

