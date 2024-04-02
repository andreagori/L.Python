from django.urls import path
from .views import visitaWebsiteInicio

urlpatterns = [
    path('', visitaWebsiteInicio, name='paginaInicio')
]