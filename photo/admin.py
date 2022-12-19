from django.contrib import admin

# Register your models here.
from .models import Photo
from django_admin_geomap import ModelAdmin


class Admin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_default_longitude = "95.1849"
    geomap_default_latitude = "64.2637"
    geomap_default_zoom = "3"
    geomap_item_zoom = "10"
    geomap_height = "300px"

admin.site.register(Photo, Admin)
