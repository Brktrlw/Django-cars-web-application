
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("pages.urls")),
    path(_("cars/"),include("cars.urls")),
    path(_("accounts/"),include("users.urls")),
    path("socialaccounts/",include("allauth.urls")),
    path(_("contancts/"), include("contact.urls")),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
