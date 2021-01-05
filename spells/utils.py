import re
import json
from os import name
from .models import Spell, Klass


def parse_number(string: str):
    re.search()


def load_json_klass(locations: str) -> None:
    with open(locations) as f:
        data = json.load(f)
        for spell in data:
            for name in spell['klass'].split(","):
                Klass.objects.get_or_create(name=name)


def load_json_spells(locations: str) -> None:
    with open(locations) as f:
        data = json.load(f)
        for spell in data:
            level= 0 if spell['level'] == "Cantrip" else spell['level'].split("-")[0][0]
            ritual= False if spell['ritual'] == 'no' else True
            concentration= False if spell['concentration'] == 'no' else True
            Spell.objects.get_or_create(
                name=spell['name'],
                desc=spell['desc'],
                page=spell['page'],
                range=spell['range'],
                components=spell['components'],
                material=spell.get("material", "N/A"),
                ritual=ritual,
                duration=spell['duration'],
                concentration=concentration,
                casting_time=spell['casting_time'],
                level=int(level),
                school=spell['school'],
            )
