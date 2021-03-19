from django.db import models

class Monster(models.Model):
    species = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    danger_level = models.IntegerField(default=0)
    features = models.JSONField(default=["REDACTED"])
    about = models.CharField(max_length=2000)
    def __str__(self):
        return self.name

class Sighting(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    date = models.DateTimeField(max_length=20)
    description = models.CharField(max_length=2000)
    day= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.monster.name}: {self.day}"

class Location(models.Model):
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    history = models.CharField(max_length=1000, default="GAREASDFASDAFASDFF")
    def __str__(self):
        return self.location
