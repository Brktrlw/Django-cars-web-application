from django.contrib import admin
from .models import CarModel
from django.utils.html import format_html



@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,obj):
        return format_html(f'<img src="{obj.car_photo_1.url}" width="100" style="border-radius:10px" />')
    thumbnail.short_description="Image"
    list_display = ("thumbnail","title","color","model","year","fuel_type",)
    search_fields = ("title",)
    list_filter = ("year","city")

