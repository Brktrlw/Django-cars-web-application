from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from cars.models import CarModel


class ContactModel(models.Model):
    first_name    = models.CharField(verbose_name=_("First Name"),max_length=100)
    last_name     = models.CharField(verbose_name=_("Last Name"),max_length=100)
    car_slug      = models.SlugField(verbose_name=_("Slug"),max_length=500)
    car           = models.ForeignKey(CarModel,verbose_name=_("Car"),on_delete=models.CASCADE)
    customer_need = models.CharField(max_length=100)
    phone         = models.CharField(max_length=15,verbose_name=_("Phone Number"))
    email         = models.CharField(verbose_name=_("Email"),max_length=100)
    city          = models.CharField(verbose_name=_("City"),max_length=100)
    state         = models.CharField(verbose_name=_("State"),max_length=100)
    message       = models.TextField(verbose_name=_("Message"))
    user          = models.ForeignKey(User,verbose_name=_("User"),on_delete=models.CASCADE)
    created_date  = models.DateTimeField(auto_now_add=True,verbose_name=_("Created Date"))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



