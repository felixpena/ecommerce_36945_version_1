"""
from django.shortcuts import render
from django.http import HttpResponse
from .models import Customize

# Create your views here.





def read_customize(request):
    custom = Customize.objects.all()
    context = {'custom': custom}
    return render(request, "base_custom.html", context)

# Método http response
def read_customize(request):
    return HttpResponse("aplicación para personalización del front para el cliente.")

"""