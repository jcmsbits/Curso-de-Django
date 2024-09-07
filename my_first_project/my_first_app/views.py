from django.shortcuts import render
from my_first_app.models import Car
from django.views.generic.base import TemplateView

# Create your views here.

def my_view(request):
    # car_list = [
    #     {"title":"BMW"},
    #     {"title":"Mazda"}
    # ]
    car_list = Car.objects.all()
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context=context)

class my_class_view(TemplateView):
    template_name = "my_first_app/car_list.html"

    # car_list = [
    #     {"title":"BMW"},
    #     {"title":"Mazda"}
    # ]
    def get_context_data(self):
        car_list = Car.objects.all()
        context = {
            "car_list": car_list
        }
        return context