from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.views.generic import DetailView
from .models import Order

# Create your views here.

class MyOrderView(LoginRequiredMixin,DetailView):
    model = Order
    template_name = "orders/my-order.html"
    context_object_name = "order"

    def get_object(self, queryset = None):
        order =Order.objects.filter(is_active = True, user = self.request.user).first()
        print(order)
        return order
