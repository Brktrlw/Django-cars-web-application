from django.db import models
from django.utils.translation import gettext_lazy as _


class TeamsModel(models.Model):
    first_name   = models.CharField(verbose_name=_("First Name"),max_length=100)
    last_name    = models.CharField(verbose_name=_("Last Name"),max_length=100)
    designation  = models.CharField(verbose_name=_("Designation"),max_length=100)
    facebook     = models.URLField(verbose_name=_("Facebook Link"),max_length=100)
    twitter      = models.URLField(verbose_name=_("Twitter Link"),max_length=100)
    google       = models.URLField(verbose_name=_("Google Link"),max_length=100)
    created_date = models.DateTimeField(verbose_name=_("Created Date"),auto_now_add=True)
    image        = models.ImageField(verbose_name=_("Image"),upload_to="teams/%Y/%m/%d/")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table            = "TeamMembers"
        verbose_name        = _("Team Member")
        verbose_name_plural = _("Team Members")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
