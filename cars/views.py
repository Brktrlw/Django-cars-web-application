from django.views.generic import ListView,DetailView
from .models import CarModel

class CarListView(ListView):

    template_name = "cars/cars.html"

    def get_queryset(self):
        pass

class CarDetailView(DetailView):
    context_object_name = "car"
    template_name = "cars/car_detail.html"

    def get_object(self, queryset=None):
        return CarModel.objects.get(slug=self.kwargs.get("slug"))


