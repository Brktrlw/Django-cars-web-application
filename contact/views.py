from django.views.generic import View,FormView
from .forms import ContactForm
from django.shortcuts import redirect


class ContactView(FormView):
    form_class = ContactForm

    def form_valid(self, form):
        user         = self.request.user
        contact      = form.save(commit=False)
        contact.user = user
        car_slug     = form.cleaned_data.get("car_slug")
        form.save()
        return redirect("url_carDetail",car_slug)




