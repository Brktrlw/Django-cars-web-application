from django.views.generic import View,FormView
from .forms import ContactForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from cars.models import CarModel

class ContactView(LoginRequiredMixin,FormView):
    form_class = ContactForm

    def form_valid(self, form):
        user         = self.request.user
        contact      = form.save(commit=False)
        contact.user = user
        car_slug     = form.cleaned_data.get("car_slug")
        car          = get_object_or_404(CarModel,slug=car_slug)
        contact.car  = car
        form.save()
        messages.success(self.request,_("Your message has beed send successfuly"))
        return redirect("url_carDetail",car_slug)




