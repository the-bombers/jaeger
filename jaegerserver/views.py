from django.shortcuts import render
from .models import Monster, Sighting, Location

from django.http import HttpResponse

def index(request):
    return HttpResponse("Monsters from Beyond")


def monsters(request):
    context = {"monsters": Monster.objects.all()}
    return render(request, "jaegerserver/monster_list.html", context)


def sightings(request):
    sightings = Sighting.objects.all()
    monsterSightings = [s.monster.species for s in sightings]
    return HttpResponse(monsterSightings)


def monsters_detail(request, monster_id):
    monster = Monster.objects.get(pk=monster_id)
    return render(request, "jaegerserver/monster_detail.html", monster)


def locations(request):


    context = {"locations": Location.objects.all()}

    return render(request, "jaegerserver/locations.html", context)


    context = {"locations": Location.objects.all()}
    return render(request, "jaegerserver/locations.html", context)


def monsterSightings(request, monsters_id):
    monster = Monster.objects.get(pk=monsters_id)
    sightingsList = monster.sighting_set.all()
    sightDay = [s.day for s in sightingsList]
    return HttpResponse(sightDay)
    # return HttpResponse(“I’m still working”)



def locations_detail(request, location_id):
    context = {"location": Location.objects.get(pk=location_id)}
    return render(request, "jaegerserver/location_detail.html", context)

