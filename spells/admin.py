from django.contrib import admin
from .models import Klass, Spell


@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Spell)
class KlassAdmin(admin.ModelAdmin):
    list_display = ['name', 'range', 'ritual', 'casting_time', 'level']
    search_fields = ['name', 'range', 'ritual', 'casting_time', 'level', 'desc']
    list_filter = ['level', 'ritual']