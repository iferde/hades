from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

# ListView con ajax para trabajar con volumen de datos
class dashboard_TemplateView(TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(login_required) # Proteger vista con login
    # El método dispatch se pueden usar para la sobre-escritura del los métodos GET y POST.
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        return context
