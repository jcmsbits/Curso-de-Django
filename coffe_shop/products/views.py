from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import FormView, ListView
from .forms import ProductForm
from .models import Products

# Create your views here.

class ProductFormView(FormView):
     template_name = "products/add_product.html"
     form_class = ProductForm
     success_url = reverse_lazy("listado")

     def form_valid(self, form):
          form.save()
          return super().form_valid(form)
     
class ProductLisView(ListView):
     model = Products
     template_name = "products/product_list.html" 
     context_object_name = "products"    

     # def get_context_data(self):
     #      list_products = Products.objects.all()
     #      return {"list_products": list_products}