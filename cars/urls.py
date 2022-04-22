from django.urls import path
from .views import CarListView,CarDetailView,SearchView
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path("",CarListView.as_view(),name="url_cars"),
    path("<slug>",CarDetailView.as_view(),name="url_carDetail"),
    path(_("search/"),SearchView.as_view(),name="url_search")
]
