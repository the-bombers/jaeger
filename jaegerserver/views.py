from django.shortcuts import render
from .models import Monster, Sighting, Location

from django.http import HttpResponse

from .models import Monster, Sighting, Location


def index(request):
    return HttpResponse("Monsters from Beyond")

def monsters(request):
    monsters = Monster.objects.all()
    return render(request, "jaegerserver/monster_list.html", monsters)

def sightings(request):
    sightings = Sighting.objects.all()
    monsterSightings = [s.monster.species for s in sightings]
    return HttpResponse(monsterSightings)

def monsters_detail(request, monster_id):
    monster = Monster.objects.get(pk=monster_id)
    return render(request, "jaegerserver/monster_detail.html", monster)

def locations(request):
    locations = Location.objects.all()
    location_list = [l.location for l in locations]
    return HttpResponse(location_list)

def monsterSightings(request, monsters_id):
    monster = Monster.objects.get(pk=monsters_id)
    sightingsList = monster.sighting_set.all()
    sightDay = [s.day for s in sightingsList]
    return HttpResponse(sightDay)
    # return HttpResponse(“I’m still working”)

    context = {"locations": Location.objects.all()}
    # location_list = [l.location for l in locations]
    return render(request, "jaegerserver/locations.html", context)