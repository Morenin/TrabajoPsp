from django.contrib.auth.views import LoginView,LogoutView



class LoginFormView(LoginView):
    template_name = 'login.html'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Iniciar sesion'
        return context

