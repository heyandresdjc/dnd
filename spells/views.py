from spells.utils import load_json_klass, load_json_spells
from django.shortcuts import render
from .models import Spell


def spell_list(request):
    # load_json_klass("spells/spells.json")
    # load_json_spells("spells/spells.json")
    spells = Spell.objects.all()
    return render(request, "spells/spell_list.html", {"object_list": spells})
