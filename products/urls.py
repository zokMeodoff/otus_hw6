from django.urls import path
from products.views import AllProductsView, OneProductView


app_name = 'products'
urlpatterns = [
     path('', AllProductsView.as_view(), name='products'),
     path('<int:pk>/', OneProductView.as_view(), name='product')
]