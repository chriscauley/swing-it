from django.db import models

_choices = lambda x: list(zip(x,x))
from .poses import LIMBS

LIMB_CHOICES = _choices(LIMBS)


class Bar(models.Model):
    name = models.CharField(max_length=64)
    data = models.JSONField(default=dict)
    __str__ = lambda self: self.name


class Pose(models.Model):
    limb = models.CharField(max_length=16, choices=LIMB_CHOICES)
    slug = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True, default='')
    __str__ = lambda self: self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
