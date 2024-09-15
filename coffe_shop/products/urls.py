from django.urls import path

from.views import ProductFormView, ProductLisView

urlpatterns = [
    path('agregar', ProductFormView.as_view(), name= "add_product"),
    path('listado', ProductLisView.as_view(), name ="listado")
]   
