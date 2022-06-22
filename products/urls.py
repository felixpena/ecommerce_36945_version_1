from django.urls import path

from products.views import List_products, Create_product, search_products, Detail_product, Delete_product, Update_product
#from products.views import dropdown_categoria


urlpatterns =[
    path('', List_products.as_view(), name = 'list_products'),

    path('create-products/', Create_product.as_view(), name = 'create_products'),
    path('search-product/', search_products, name = 'search_products'),
    path('detail-product/<int:pk>/', Detail_product.as_view(), name = 'detail_product'),
    path('delete-product/<int:pk>/', Delete_product.as_view(), name = 'delete_product'),
    path('update-product/<int:pk>/', Update_product.as_view(), name = 'update_product'),

    #path('dropdown/', dropdown_categoria, name = 'dropdown_categoria'),
    #path('', List_products_categoria.as_view(), name = 'list_products'),

]

"""
from products.views import List_products_categoria

urlpatterns =[
    path('list_products_categoria', List_products_categoria, name = 'list_products_categoria'),
]
"""