from django.shortcuts import render
from .models import Monster, Sighting, Location


from django.http import HttpResponse

from .models import Monster, Sighting


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

    context = {"locations": Location.objects.all()}
    # location_list = [l.location for l in locations]
    return render(request, "jaegerserver/locations.html", context)


def monsterSightings(request, monsters_id):
    monster = Monster.objects.get(pk=monsters_id)
    # monsterId = monsters()
    # return HttpResponse(“I’m still working”)
    return HttpResponse(monster.id)
