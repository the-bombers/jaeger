from django.shortcuts import render
from .models import Monster, Sighting


from django.http import HttpResponse


def index(request):
    monsters = Monster.objects.all()
    mns = ", ".join([m.species for m in monsters])
    return HttpResponse(mns)


def sightings(request):
    sightings = Sighting.objects.all()
    monsterSightings = [s.monster.species for s in sightings]
    return HttpResponse(monsterSightings)


def locations(request):
    locations = Locations.objects.all()
    monsterLocation = [l.monster.sighting for l in locations]
    return HttpResponse(monsterLocation)
