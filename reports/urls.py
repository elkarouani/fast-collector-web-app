from django.urls import path
from .views import FormView, ExportView


urlpatterns = [
    path('form/', FormView, name='form_view'),
    path('export/', ExportView, name='export_view'),
]
