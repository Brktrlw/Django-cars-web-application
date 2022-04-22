from django.contrib import admin
from .models import ContactModel


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","message")
    list_display_links = ("first_name",)



