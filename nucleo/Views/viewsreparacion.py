from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View,FormView
from nucleo.models import Coche, Reparacion
from nucleo.forms import ReparacionForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from nucleo.mixins import *


import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from nucleo.user.models import User

# Create your views here.


class ReparacionListView(ListView):
    model=Reparacion
    template_name='reparacion/index.html'
    


    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Listado de reparaciones'
        context['object_list']=Reparacion.objects.all()
        context['create_url']= reverse_lazy('reparacion_create')
        context['index']=reverse_lazy('reparacion_list')
        context['entity']='Reparaciones'
        return context

class ReparacionCreateView(CreateView):
    model=Reparacion 
    form_class=ReparacionForm
    template_name='reparacion/create.html'
    succes_url= reverse_lazy('reparacion_list')

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        cliente = self.request.user
        form= ReparacionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Id_Cliente = cliente
            form.save()
            return HttpResponseRedirect(self.succes_url)
        self.object=None
        context = self.get_context_data(**kwargs)
        context['form']= form
        
        return render(request,self.template_name,context)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Añadir una reparacion'
        context['entity']='Reparaciones'
        context['index']=reverse_lazy('reparacion_list')
        context['form']=ReparacionForm
        return context

    
class ReparacionUpdateView(GroupRequiredMixin,UpdateView):
    model=Reparacion  
    form_class=ReparacionForm
    template_name='reparacion/create.html'
    succes_url= reverse_lazy('reparacion_list')
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
        context['title'] = 'Modificando una reparacion'
        context['entity']='Reparaciones'
        context['index']=reverse_lazy('reparacion_list')
        context['action']='edit'
        return context

   

class ReparacionDeleteView(GroupRequiredMixin,DeleteView):
    model = Reparacion
    form_class=ReparacionForm
    template_name='reparacion/delete.html'
    succes_url= reverse_lazy('reparacion_list')
    group_required=u"Mecanico"

    def get_querryset(self,request):
        if not request.user.is_superuser:
            return False

    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Eliminando ua reparacion'
        context['entity']='Reparaciones'
        context['index']=reverse_lazy('reparacion_list')
        return context

class ReparacionPDFView(View):
    model=Reparacion

    def link_callback(self, uri, rel):
        sUrl = settings.STATIC_URL  
        sRoot = settings.STATIC_ROOT  
        mUrl = settings.MEDIA_URL  
        mRoot = settings.MEDIA_ROOT  

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  

        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request,*args,**kwargs):
        try:
            template = get_template('reparacion/pdf.html')
            context={
                'rep' : Reparacion.objects.get(pk=self.kwargs['pk']),
                'icon': '{}{}'.format(settings.STATIC_URL, 'img/logo.jpg')
            }
            html =template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reparacion.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response,link_callback=self.link_callback)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('reparacion_list'))


    