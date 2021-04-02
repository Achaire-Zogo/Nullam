from django.contrib import admin
from .models import Event, ticket, OrderEvent
from mapbox_location_field.admin import MapAdmin


# class EventsAdmin(admin.ModelAdmin):
#     list_display = ('titre', 'description', 'photo', 'price')


admin.site.register(Event, MapAdmin)
admin.site.register(ticket)

# admin.site.register(Event)

