from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
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
