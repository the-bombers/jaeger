from django.shortcuts import render
from .models import Monster, Sighting


from django.http import HttpResponse
def index(request):
    return HttpResponse("Monsters from Beyond") 

def monsters(request):
    monsters = Monster.objects.all()
    mns = ", ".join([m.species for m in monsters])
    return HttpResponse(mns) 

def sightings(request):
    sightings = Sighting.objects.all()
    monsterSightings = [s.monster.species for s in sightings]
    return HttpResponse(monsterSightings)

def monsters_detail(request, monster_id):
    monster = Monster.objects.get(pk=monster_id)
    return render(request, "jaegerserver/monster_detail.html", monster)