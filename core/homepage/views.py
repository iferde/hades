from django.views.generic import TemplateView

# Create your views here.

# Vista genérica para renderizar un template
class IndexView(TemplateView):
    template_name = 'index.html'
