from django.forms import *
from nucleo.user.models import User


class UserForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']='form-control'
            form.field.widget.attrs['autocomplete']='off'

    class Meta:
        model=User
        fields='first_name', 'last_name', 'Dni','email', 'username', 'password','groups'
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'Dni':TextInput(
                attrs={
                    'placeholder':'Ingrese su DNI'
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese su email',
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese su username',
                }
            ),
            'password': PasswordInput(render_value=True,
                attrs={
                    'placeholder': 'Ingrese su password',
                }
            ),
            'groups': Select(attrs={'style':'width 100%'})
            
        }
        exclude = {'is_staff','is_active','is_superuser','Direccion','user_permissions','last_login','date_joined'}