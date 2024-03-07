from django.views.generic import TemplateView

# Create your views here.

# ListView con ajax para trabajar con volumen de datos
class dashboard_TemplateView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        return context
