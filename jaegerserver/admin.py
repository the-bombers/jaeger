from django.contrib import admin

from jaegerserver.models import Monster, Sighting

admin.site.register(Monster)
admin.site.register(Sighting)
