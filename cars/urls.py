from django.urls import path
from .views import CarListView,CarDetailView

urlpatterns = [
    path("",CarListView.as_view(),name="url_cars"),
    path("<slug>",CarDetailView.as_view(),name="url_carDetail")
]
