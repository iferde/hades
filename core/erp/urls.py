from django.urls import path
from core.erp.views.dashboard.views import *

app_name = 'erp'

urlpatterns = [
    # Home
    path('dashboard/', dashboard_TemplateView.as_view(), name='dashboard'),
]

