from django.contrib import admin
from .models import Event, Ticket, OrderEvent, AchatTicket, Cathegorie, Publish, OrderEvent, Order, ShippinrAddress
from mapbox_location_field.admin import MapAdmin

# class EventsAdmin(admin.ModelAdmin):
#     list_display = ('titre', 'description', 'photo', 'price')


admin.site.register(Event, MapAdmin)
admin.site.register(Ticket)
admin.site.register(Cathegorie)
admin.site.register(Publish)
admin.site.register(Order)
admin.site.register(OrderEvent)
admin.site.register(AchatTicket)
admin.site.register(ShippinrAddress)
