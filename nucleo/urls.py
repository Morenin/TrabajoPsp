from django.urls import path

from nucleo.Views.viewscoches import *
from nucleo.Views.viewsnoticias import *

from nucleo.Views.viewsreparacion import *
from nucleo.login.views import *
from nucleo.Views.views import DashboardView
from nucleo.user.views import *
urlpatterns = [
# Login
    path('login/',LoginFormView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
# Usuarios
    path('user/list',UserListView.as_view(), name="user_list"),
    path('user/add',UserCreateView.as_view(), name="user_create"),
    path('user/edit/<int:pk>',UserUpdateView.as_view(success_url="/user/list"), name="user_edit"),
    path('user/delete/<int:pk>',UserDeleteView.as_view(success_url="/user/list"), name="user_delete"),  
#API
    path('api/user', UserAPI.as_view()),
    path('api/user/<int:pk>/',UserAPIdetail.as_view()),
    path('api/token/',TestView.as_view()),
# Coches
    path('coche/list',CocheListView.as_view(), name="coche_list"),
    path('coche/add',CocheCreateView.as_view(), name="coche_create"),
    path('coche/edit/<int:pk>',CocheUpdateView.as_view(success_url="/coche/list"), name="coche_edit"),
    path('coche/delete/<int:pk>',CocheDeleteView.as_view(success_url="/coche/list"), name="coche_delete"),
# Noticia
    path('noticia/list',NoticiaListView.as_view(), name="noticia_list"),
    path('noticia/add',NoticiaCreateView.as_view(), name="noticia_create"),
    path('noticia/edit/<int:pk>',NoticiaUpdateView.as_view(success_url="/noticia/list"), name="noticia_edit"),
    path('noticia/delete/<int:pk>',NoticiaDeleteView.as_view(success_url="/noticia/list"), name="noticia_delete"),
# Reparacion
    path('reparacion/list',ReparacionListView.as_view(), name="reparacion_list"),
    path('reparacion/add',ReparacionCreateView.as_view(), name="reparacion_create"),
    path('reparacion/edit/<int:pk>',ReparacionUpdateView.as_view(success_url="/reparacion/list"), name="reparacion_edit"),
    path('reparacion/delete/<int:pk>',ReparacionDeleteView.as_view(success_url="/reparacion/list"), name="reparacion_delete"),
    path('reparacion/pdf/<int:pk>',ReparacionPDFView.as_view(), name="reparacion_pdf"),
   
]
