from django.urls import path
from core.erp.views.dashboard.views import *
from core.erp.views.category.views import *
from core.erp.views.product.views import *
from core.erp.views.client.views import *
from core.erp.views.test.views import TextView

app_name = 'erp'

urlpatterns = [
    # Home
    path('dashboard/', dashboard_TemplateView.as_view(), name='dashboard'),
    # Category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # client
    path('client/', ClientView.as_view(), name='client'),
    # test
    path('test/', TextView.as_view(), name='test'),
]
