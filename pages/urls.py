
from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import (HomePageView,AboutPageView,ServicesPageView,ContactView)

urlpatterns = [
    path("",HomePageView.as_view(),name="url_homepage"),
    path(_("about/"),AboutPageView.as_view(),name="url_aboutpage"),
    path(_("services/"),ServicesPageView.as_view(),name="url_servicespage"),
    path(_("contact/"),ContactView.as_view(),name="url_contact")
]
