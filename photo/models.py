from django.contrib.auth.models import User
from django.db import models
from django_admin_geomap import GeoItem


class Photo(models.Model, GeoItem):

    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)

    @property
    def geomap_icon(self):
        return self.default_icon

    @property
    def geomap_popup_view(self):
        return "<strong>{}</strong>".format(str(self))

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view

    image = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    location_name = models.CharField(max_length=100, null=True)
    lon = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True)
    people_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.date}, {self.description}"
