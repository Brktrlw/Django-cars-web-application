from django.views.generic import ListView,DetailView,View
from .models import CarModel
from django.db.models import Q

class CarListView(ListView):
    template_name       = "cars/cars.html"
    paginate_by         = 2
    context_object_name = "cars"

    def get_queryset(self):
        return CarModel.objects.filter(is_featured=True).order_by("-created_date")


class CarDetailView(DetailView):
    context_object_name = "car"
    template_name = "cars/car_detail.html"

    def get_object(self, queryset=None):
        return CarModel.objects.get(slug=self.kwargs.get("slug"))


class SearchView(ListView):
    context_object_name = "cars"
    template_name       = "cars/search.html"

    def get_queryset(self):
        keyword   = self.request.GET.get("keyword")
        model     = self.request.GET.get("model")
        year      = self.request.GET.get("year")
        body      = self.request.GET.get("body")
        city      = self.request.GET.get("city")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        cars = CarModel.objects.filter(title__icontains=keyword)
        if model:
            cars = cars.filter(model__iexact = model)
        if year:
            cars = cars.filter(year = year)
        if city:
            cars = cars.filter(city__iexact = city)
        if body:
            cars = cars.filter(body_style__iexact=body)
        cars = cars.filter(price__gte=min_price,price__lte=max_price)
        return cars