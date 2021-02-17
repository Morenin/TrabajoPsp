from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from nucleo.user.models import User
from nucleo.user.forms import UserForm
from rest_framework.views import APIView
from nucleo.user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.exceptions import ParseError
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserListView(ListView):
    model=User
    template_name='listado.html'
    
    # @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Listado de usuarios'
        context['object_list']=User.objects.all()
        context['create_url']= reverse_lazy('user_create')
        context['index']=reverse_lazy('user_list')
        context['entity']='Usuarios'
        # context['groups']=User.groups.filter(User)
        return context

class UserCreateView(CreateView):
    
    model=User 
    form_class=UserForm
    template_name='create.html'
    succes_url= reverse_lazy('user_list')
    
    
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.succes_url)
        self.object=None
        context = self.get_context_data(**kwargs)
        context['form']= form
        return render(request,self.template_name,context)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Regristate'
        context['entity']='Usuarios'
        context['index']=reverse_lazy('user_list')
        return context
        
class UserUpdateView(UpdateView):
    model=User  
    form_class=UserForm
    template_name='create.html'
    succes_url= reverse_lazy('user_list')
   
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        self.object=self.get_object()
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Modificando un usuario'
        context['entity']='Usuarios'
        context['index']=reverse_lazy('user_list')
        context['action']='edit'
        return context

class UserDeleteView(DeleteView):
    model = User
    form_class=UserForm
    template_name='delete.html'
    succes_url= reverse_lazy('user_list')
    
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Eliminando un usuario'
        context['entity']='Usuarios'
        context['index']=reverse_lazy('user_list')
        return context


class UserAPI(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request, format=None,*args,**kwargs):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPIdetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self,request,pk,format=None):
        user= self.get_object(pk)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk, format=None):
        user= self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TestView(APIView):

    def get(self,request, format=None):
        return Response({'detail': "GET Response"})

    def post(self,request, format=None):
        try:
            data = request.data 
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status=status.HTTP_400_BAD_REQUEST
            )
        if "user" not in data or "password" not in data:
            return Response(
                'Wrong credentials',
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        user = User.objects.get(username=data["user"])
        if not user:
            return Response(
                'No default user, please create one',
                status=status.HTTP_404_NOT_FOUND
            )
        
        token = Token.objects.get_or_create(user=user)
        return Response({'detail': 'POST answer', 'token': token[0].key})