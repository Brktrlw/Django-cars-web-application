from django.contrib import admin
from .models import TeamsModel
from django.utils.html import format_html

@admin.register(TeamsModel)
class TeamsAdmin(admin.ModelAdmin):
    def thumbnail(self,obj):
        return format_html(f'<img src="{obj.image.url}" width="40" style="border-radius:10px" />')

    thumbnail.short_description = "Photo"
    list_display       = ("thumbnail","first_name","last_name","designation")
    list_display_links = ("thumbnail","first_name")
    search_fields      = ("first_name","designation")
    list_filter        = ("designation",)






