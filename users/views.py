"""
import users
from .models import User_profile
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
"""

"""
# Lista basada en class /////   by felix  una vista del perfil de usuario.  # 
# #########no funciono, entrega el perfil de todos los usuarios.  #####

class User_profile(ListView):
    model = User_profile
    template_name = "user_profile.html"
    queryset = User_profile.objects.all()
    print(User_profile.dni)
    #queryset = Products.objects.filter(is_active = True)

########################################################################
"""

"""
# Lista basada en funcición.  Método Rendering /////   by felix  una vista del perfil de usuario.

def user_profile(request):
    lista_persona = User_profile.objects.all()
    context = {'lista_persona': lista_persona}
    print(lista_persona)
    return render(request, "user_profile.html", context)
"""


