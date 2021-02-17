from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from nucleo.models import Coche
from nucleo.forms import CocheForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from nucleo.user.models import User
from nucleo.mixins import *


class CocheListView(GroupRequiredMixin,ListView):
    model=Coche
    template_name='coche/index.html'
    group_required=u"Cliente"

    def get_querryset(self,request):
        if not request.user.is_superuser:
            return False

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Listado de coche'
        context['object_list']=Coche.objects.all()
        context['create_url']= reverse_lazy('coche_create')
        context['index']=reverse_lazy('coche_list')
        context['entity']='Coches'
        
        return context

class CocheCreateView(GroupRequiredMixin,CreateView):
    model=Coche 
    form_class=CocheForm
    field= ['Id_Cliente']

    template_name='coche/create.html'
    succes_url= reverse_lazy('coche_list')
    group_required=u"Cliente"

    def get_querryset(self,request):
        if not request.user.is_superuser:
            return False
    
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        cliente = self.request.user

        form= CocheForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Cliente_id = cliente
            form.save()
            return HttpResponseRedirect(self.succes_url)
        self.object=None
        context = self.get_context_data(**kwargs)
        context['form']= form
        return render(request,self.template_name,context)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Añadir un coche'
        context['entity']='Coches'
        context['index']=reverse_lazy('coche_list')
        return context

    # def get_queryset(self):
    #      return Coche.objects.filter(Id_Mecanico = )

    
       

class CocheUpdateView(GroupRequiredMixin,UpdateView):
    model=Coche  
    form_class=CocheForm
    template_name='coche/create.html'
    succes_url= reverse_lazy('coche_list')
    group_required=u"Cliente"

    def get_querryset(self,request):
        if not request.user.is_superuser:
            return False

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        self.object=self.get_object()
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Modificando un coche'
        context['entity']='Coche'
        context['index']=reverse_lazy('coche_list')
        context['action']='edit'
        return context

class CocheDeleteView(GroupRequiredMixin,DeleteView):
    model = Coche
    form_class=CocheForm
    template_name='coche/delete.html'
    succes_url= reverse_lazy('coche_list')
    group_required=u"Cliente"

    def get_querryset(self,request):
        if not request.user.is_superuser:
            return False

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Eliminando un coche'
        context['entity']='Coches'
        context['index']=reverse_lazy('coche_list')
        return context