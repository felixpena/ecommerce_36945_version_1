from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User_profile
from django.views.generic import UpdateView

"""
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
"""
class Update_user_profile(LoginRequiredMixin, UpdateView):
    model = User_profile
    template_name = 'update_user_profile.html'
    fields = ['phone', 'dni', 'address']
#para todo:   '__all__'

    def get_success_url(self):
        return reverse('user_profile')

# https://docs.djangoproject.com/en/4.0/ref/urlresolvers/