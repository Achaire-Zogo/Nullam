from django.contrib import admin
from .models import Event, OrderEvent


class NullamAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'photo', 'price')


admin.site.register(Event,NullamAdmin)
