from django.views.generic import TemplateView
from nucleo.models import Noticia
from nucleo.forms import NoticiaForm

class DashboardView(TemplateView):
    model=Noticia 
    form_class=NoticiaForm
    template_name='dashboard.html'

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Listado de noticias'
        context['object_list']=Noticia.objects.all()
        context['entity']='Noticias'
        return context