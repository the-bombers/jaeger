from django.contrib import admin

from jaegerserver.models import Monster, Sighting, Location

admin.site.register(Monster)
admin.site.register(Sighting)
admin.site.register(Location)
