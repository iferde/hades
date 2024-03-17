from django.urls import path
from core.erp.views.dashboard.views import *
from core.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    # Home
    path('dashboard/', dashboard_TemplateView.as_view(), name='dashboard'),
    # Category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]
