from django.views.generic import ListView


class CarListView(ListView):
    template_name = "cars/cars.html"

    def get_queryset(self):
        return




