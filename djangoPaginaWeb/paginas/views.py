from django.shortcuts import render
from django.views.generic import TemplateView  # Import TemplateView


# Create your views here.
class PaginasConfig(TemplateView):
    template_name = "paginaInicio.html"  # you put the name of your html.


class PaginasAcercaConfig(TemplateView):
    template_name = "paginas/about.html"  # you put the name of your html.
