from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('sightings/', views.sightings, name="sightings"),
    path('monsters/<int:monster_id>/',
         views.monsters_detail, name="monsters_details"),
    path("monsters/", views.monsters, name="monsters"),
    path("locations/", views.locations, name="locations"),
]
