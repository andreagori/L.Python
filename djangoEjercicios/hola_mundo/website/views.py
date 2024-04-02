from django.shortcuts import render

# ingresar esto:
from django.http import HttpResponse


# Create your views here.
# ingresamos este codigo
def visitaWebsiteInicio(solicitud):
    return HttpResponse("Hola Mundo!")
