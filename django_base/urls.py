from django.contrib import admin
from django.urls import path, include
from django_base.views import saludo, index, fecha_actual, probando_template, contact, login_view, logout_view, register_view, user_profile

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('saludo/<nombre>/', saludo, name = 'saludo'),
    path('fecha_actual/', fecha_actual, name = 'fecha_actual'),
    path('probando-template/', probando_template, name = 'probando_template'),
    path('contact/', contact, name = 'contact'),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),

    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
    
    path('user_profile/', user_profile, name = 'user_profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# //////  path para la app customize
"""
urlpatterns += [
    path('', include('customize.urls')),
    
]

"""
#  incorporar productos en el index.  Solo agregue este path que es el mismo path en urls de la app de producos y anule el patch principal de arriba el index
from products.views import List_products
urlpatterns +=[
    path('', List_products.as_view(), name = 'list_products'),]