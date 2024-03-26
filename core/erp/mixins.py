from django.shortcuts import redirect
from datetime import datetime
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

class IsSuperuserMixin(object):
    def dispatch (self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.now()
        return context
    
class ValidarPermisosMixin(object):
    permission_required = ''
    url_redirect = None

    def get_permisos(self):
        #Asignamos a perms todos los permisos en formato tupla.
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms
    
    def get_url_redireccion(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect
    
    def dispatch (self, request, *args, **kwargs):
        if request.user.has_perms(self.get_permisos()): #Usamos la propiedad has_perms para recorrer todos los permisos
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, "No tiene permiso a ingresar a este módulo")
        return HttpResponseRedirect(self.get_url_redireccion()) #Podemos usar también redirect
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.now()
        return context
