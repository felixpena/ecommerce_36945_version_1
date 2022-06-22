from .models import Customize

def read_customize(request):
    custom = Customize.objects.all()
    context = {'custom': custom}
    return (context)



from products.models import Categoria

def dropdown_categoria(request):
    categoria = Categoria.objects.all()
    context = {'categoria': categoria}
    return (context)

# https://www.youtube.com/watch?v=_eWLaL2g1bo