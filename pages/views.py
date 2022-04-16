from django.shortcuts import render
from django.views.generic import (
TemplateView,View,ListView,FormView
)
from teams.models import TeamsModel

class HomePageView(View):
    http_method_names = ["get"]

    def get(self,request):
        ctx = {"team_members":self.get_team_members()}
        return render(request,"pages/homepage.html",ctx)

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


