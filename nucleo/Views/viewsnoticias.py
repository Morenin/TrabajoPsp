from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from nucleo.models import Noticia
from nucleo.forms import NoticiaForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from nucleo.mixins import *
# Create your views here.


class NoticiaListView(GroupRequiredMixin,ListView):
    model=Noticia
    template_name='noticia/index.html'

    group_required=u"Mecanico"

    def get_querryset(self,request):
        if not request.user.is_superuser:
            return False

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Listado de noticias'
        context['object_list']=Noticia.objects.all()
        context['create_url']= reverse_lazy('noticia_create')
        context['index']=reverse_lazy('noticia_list')
        context['entity']='Noticias'
        return context

class NoticiaCreateView(GroupRequiredMixin,CreateView):
    model=Noticia 
    form_class=NoticiaForm
    template_name='noticia/create.html'
    succes_url= reverse_lazy('noticia_list')
    group_required=u"Mecanico"

    def get_querryset(self,request):
        if not request.user.is_superuser:
            return False

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        mecanico = self.request.user
        form= NoticiaForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Id_Mecanico = mecanico
            form.save()
            return HttpResponseRedirect(self.succes_url)
        self.object=None
        context = self.get_context_data(**kwargs)
        context['form']= form
        return render(request,self.template_name,context)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Añadir una noticia'
        context['entity']='Noticias'
        context['index']=reverse_lazy('noticia_list')
        return context
    
class NoticiaUpdateView(GroupRequiredMixin,UpdateView):
    model=Noticia 
    form_class=NoticiaForm
    template_name='noticia/create.html'
    succes_url= reverse_lazy('noticia_list')
    group_required=u"Mecanico"

    def get_querryset(self,request):
        if not request.user.is_superuser:
            return False

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        self.object=self.get_object()
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Modificando una noticia'
        context['entity']='Noticias'
        context['index']=reverse_lazy('noticia_list')
        context['action']='edit'
        return context

class NoticiaDeleteView(GroupRequiredMixin,DeleteView):
    model = Noticia
    form_class=NoticiaForm
    template_name='noticia/delete.html'
    succes_url= reverse_lazy('noticia_list')
    group_required=u"Mecanico"

    def get_querryset(self,request):
        if not request.user.is_superuser:
            return False

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Eliminando una noticia'
        context['entity']='Noticias'
        context['index']=reverse_lazy('noticia_list')
        return context