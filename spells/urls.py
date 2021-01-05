from spells.models import Spell
from django.views.generic.list import ListView
from django.urls import path
from .views import spell_list

app_name = 'spells'
urlpatterns = [
    path('', spell_list, name="spell_list")
]
