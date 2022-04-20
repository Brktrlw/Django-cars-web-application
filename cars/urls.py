from django.urls import path
from .views import CarListView,CarDetailView,SearchView

urlpatterns = [
    path("",CarListView.as_view(),name="url_cars"),
    path("<slug>",CarDetailView.as_view(),name="url_carDetail"),
    path("search/",SearchView.as_view(),name="url_search")
]
