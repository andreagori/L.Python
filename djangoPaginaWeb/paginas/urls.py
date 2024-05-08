from django.urls import path
from .views import PaginasConfig, PaginasAcercaConfig  # we import the views

urlpatterns = [
    path("", PaginasConfig.as_view(), name="paginaInicio"),  # we add the path to the home page
    path("about/", PaginasAcercaConfig.as_view(), name="paginaAcercaDe"),  # we add the path to the about page
]
