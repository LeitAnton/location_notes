from django.db import models
from django.contrib.auth import get_user_model
import folium

User = get_user_model()


class Map(models.Model):
    longitude = models.FloatField(default=27.54529846070204)
    latitude = models.FloatField(default=53.90519401495765)
    zoom_start = models.IntegerField(default=6)
    tiles = models.CharField(max_length=100, default="Mapbox Bright")


class Marker(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    popup = models.CharField(max_length=50)


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    map = models.ForeignKey(Map, on_delete=models.CASCADE, verbose_name="Map", auto_created=True)
    markers = models.ManyToManyField(Marker, related_name="Marker", null=True)

