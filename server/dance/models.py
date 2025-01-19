from django.db import models

_choices = lambda x: list(zip(x,x))

LIMB_CHOICES = _choices(['arm', 'leg', 'torso', 'facing'])

class Pose(models.Model):
    limb = models.CharField(max_length=8, choices=LIMB_CHOICES)
    slug = models.CharField(max_length=16)
    name = models.CharField(max_length=16)
    description = models.TextField(blank=True, default='')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return
