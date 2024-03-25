from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.generic import TemplateView
from core.erp.models import Product,Category

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
            print(action)
            if action == 'search_product_id':
                data = []
                for i in Product.objects.filter(cat_id=request.POST['id']):
                    data.append({'id': i.id,'name':i.name})
            elif action == 'search_product_id_2':
                data = [{'id':'', 'text':'-------------'}]
                for i in Product.objects.filter(cat_id=request.POST['id']):
                    data.append({'id': i.id,'text':i.name,'data':i.cat.toJSON()}) # La última variable trae todo el objeto
            elif action == 'autocomplete':
                data = []                
                for i in Category.objects.filter(name__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.name
                    data.append(item) # La última variable trae todo el objeto
            elif action == 'autocomplete_2':
                data = []                
                for i in Category.objects.filter(name__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.name
                    data.append(item) # La última variable trae todo el objeto
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False) # safe=False para trabajar con colección de elementos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Anidados | Django'
        context['title2'] = 'Select Anidados (con select2) | Django'
        context['title3'] = 'Autocompletado (con jquery UI) | Django'
        context['title4'] = 'Autocompletado (con select2) | Django'
        context['form'] = TestForm()
        return context
