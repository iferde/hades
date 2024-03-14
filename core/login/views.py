from typing import Any
from django import http
import config.settings as settings
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView

# Vista genérica de login
class LoginFormView(LoginView):
    template_name = 'login.html'

     # Usamos este método para redireccionar y el login es correcto.
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio de sesión'        
        return context

# Realizar Login con FormView (permite editar y realizar más acciones)
class LoginFormView2(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    # Usamos este método para redireccionar y el login es correcto.
    def dispatch(self, request, *args, **kwargs):
        #if request.user.is_authenticated:
        #    return redirect('erp:category_list')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio de sesión'        
        return context

class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)