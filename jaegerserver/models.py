from django.db import models

class Monster(models.Model):
    species = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Sighting(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)

class Location(models.Model):
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
