from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.generic import TemplateView
from core.erp.models import Product

from core.erp.forms import TestForm

class TextView(TemplateView):
    template_name = 'tests.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required) # Proteger vista con login
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = []
                for i in Product.objects.filter(cat_id=request.POST['id']):
                    data.append({'id': i.id,'name':i.name})
            elif action == 'search_product_id_2':
                data = [{'id':'', 'text':'-------------'}]
                for i in Product.objects.filter(cat_id=request.POST['id']):
                    data.append({'id': i.id,'text':i.name,'data':i.cat.toJSON()}) # La última variable trae todo el objeto
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False) # safe=False para trabajar con colección de elementos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Anidados | Django'
        context['title2'] = 'Select Anidados (con select2) | Django'
        context['form'] = TestForm()
        return context
