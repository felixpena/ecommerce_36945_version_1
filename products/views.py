from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Categoria, Products
from products.forms import Product_form

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class List_products(ListView):
    model = Products
    template_name= 'products.html'
    queryset = Products.objects.filter(is_active = True,)

class Detail_product(DetailView):
    model = Products
    template_name= 'detail_product.html'

class Create_product(LoginRequiredMixin, CreateView):
    model = Products
    template_name = 'create_products.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk':self.object.pk})

class Delete_product(LoginRequiredMixin, DeleteView):
    model = Products
    template_name = 'delete_product.html'

    def get_success_url(self):
        return reverse('list_products')

class Update_product(LoginRequiredMixin, UpdateView):
    model = Products
    template_name = 'update_product.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_product', kwargs = {'pk':self.object.pk})



# Create your views here.       
# def list_products(request):
#     products = Products.objects.all()
#     context = {'products':products}
#     return render(request, 'products.html', context=context)

# def detail_product(request, pk):
#     try:
#         product = Products.objects.get(id=pk)
#         context = {'product':product}
#         return render(request, 'product_detail.html', context=context)
#     except:
#         context = {'error':'El Producto no existe'}
#         return render(request, 'products.html', context=context)

# def create_products(request):
#     if request.method == 'GET':

#         form = Product_form()
#         context = {'form':form}

#         return render(request, 'create_products.html', context=context)

#     elif request.method == 'POST':
        
#         form = Product_form(request.POST)
#         if form.is_valid():
#             new_product = Products.objects.create(
#                 name = form.cleaned_data['name'],
#                 price = form.cleaned_data['price'],
#                 description = form.cleaned_data['description'],
#                 SKU = form.cleaned_data['SKU'],
#                 is_active = form.cleaned_data['is_active'],
#             )
#             context = {'new_product':new_product}
#         else:
#             context = {'errors':form.errors}
#         return render(request, 'create_products.html', context = context)

#     else:
#         return HttpResponse('Only GET and POST methods are allowed')



# def delete_product(request, pk):
#     try:
#         if request.method == 'GET':
#             product = Products.objects.get(id=pk)
#             context = {'product':product}
#         else:
#             product = Products.objects.get(id=pk)
#             product.delete()
#             context = {'message':'Producto eliminado correctamente'}

#         return render(request, 'delete_product.html', context=context)

#     except:
#         context = {'error':'El Producto no existe'}
#         return render(request, 'delete_product.html', context=context)



def search_products(request):
    products = Products.objects.filter(name__icontains=request.GET['search'])
    if products.exists():
        context = {'products':products}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'search_products.html', context = context)

"""
# funcion listar categoria
def dropdown_categoria(request):
    categoria = Categoria.objects.all()
    context = {'categoria':categoria}
    
    return render(request, 'base.html', context=context)
"""
"""
class List_products_categoria(ListView):
    model = Products
    template_name= 'categorias/filter.html'
    queryset = Products.objects.filter()


def List_products_categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    listado = categoria.products.all()
    context ={
        'categoria': categoria,
        'productos': listado
    }
    return render(request, 'categoria/filter2.html', context)
"""