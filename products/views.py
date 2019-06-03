from django.views.generic import ListView, DetailView
from products.models import Product


class AllProductsView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products_list'


class OneProductView(DetailView):
    model = Product
    template_name = 'products/product.html'



