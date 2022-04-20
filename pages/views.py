from django.shortcuts import render
from django.views.generic import (
TemplateView,View
)
from cars.models import CarModel
from teams.models import TeamsModel

class BaseSearchView(View):
    def get_search_fields(self):
        ctx = {
        "model_fields"    : CarModel.objects.values("model").distinct("model"),
        "city_fields"     : CarModel.objects.values("city").distinct("city"),
        "year_fields"     : CarModel.objects.values("year").distinct("year"),
        "body_fields"     : CarModel.objects.values("body_style").distinct("body_style"),
        "transmission"    : CarModel.objects.values("transmission").distinct("transmission")
        }
        return ctx

class HomePageView(BaseSearchView):
    http_method_names = ["get"]

    def get(self,request):
        ctx                  = {
            "team_members"  : self.get_team_members(),
            "featured_cars" : self.get_featured_cars(),
            "latest_cars"   : self.get_latest_cars(),
            "search_fields" : self.get_search_fields()
        }
        return render(request,"pages/homepage.html",ctx)

    def get_featured_cars(self):
        return CarModel.objects.filter(is_featured=True).order_by("-created_date")

    def get_latest_cars(self):
        return CarModel.objects.all().order_by("-created_date")[:3]

    def get_team_members(self):
        return TeamsModel.objects.all()


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    def get_context_data(self, **kwargs):
        ctx = super(AboutPageView, self).get_context_data(**kwargs)
        ctx["team_members"] = TeamsModel.objects.all()
        return ctx


class ServicesPageView(TemplateView):
    template_name = "pages/services.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"


