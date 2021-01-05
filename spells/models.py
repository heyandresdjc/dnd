import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at', )

    def __str__(self) -> str:
        return f"{self.name}"

class Klass(BaseModel):
    name = models.CharField(max_length=200)


class Spell(BaseModel):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1200)
    page = models.CharField(max_length=200)
    range = models.CharField(max_length=200)
    components = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    ritual = models.BooleanField(default=False)
    duration = models.CharField(max_length=100)
    concentration = models.BooleanField(default=False)
    casting_time = models.CharField(max_length=200)
    level = models.PositiveSmallIntegerField(default=0)
    school = models.CharField(max_length=100)
    klass = models.ManyToManyField(Klass)
