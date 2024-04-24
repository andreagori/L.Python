from django.urls import path
from .views import PaginaInicio, PaginaAcercaDe  # we import the views

urlpatterns = [
    path("", PaginaInicio.as_view(), name="paginaInicio"),  # we add the path to the home page
    path("about/", PaginaAcercaDe.as_view(), name="paginaAcercaDe"),  # we add the path to the about page
]
