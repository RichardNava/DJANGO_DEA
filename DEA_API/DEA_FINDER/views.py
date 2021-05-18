from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "DEA_FINDER/index.html")

def contact(request):
    return HttpResponse("Se encuentra en la página de contactos")

