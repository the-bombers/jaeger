from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("monsters/", views.index, name="monsters"),
    path('sightings/', views.sightings, name="sightings"),
    path("locations/", views.locations, name="locations"),
]
