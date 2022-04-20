
from django.urls import path
from .views import LoginView,RegisterView,LogoutView,DashboardView
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_("login/"),LoginView.as_view(),name="url_login"),
    path(_("register/"), RegisterView.as_view(), name="url_register"),
    path(_("logout/"), LogoutView.as_view(), name="url_logout"),
    path(_("dashboard/"), DashboardView.as_view(), name="url_dashboard")
]
