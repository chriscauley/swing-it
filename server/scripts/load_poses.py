import sys, os, django
sys.path.append('.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()

from dance.models import Pose
from dance.poses import LIMB_BY_POSE

LC_OUT_HEART = [
    "lc_chin",
    "lc_backpack",
    "lc_elbows",
    "lc_cast",
    "lc_swing",
]

LC_FMOON = [
    "lc_sky",
    "lc_out",
    "lc_earth",
    "lc_chest",
]

for slug, limb in LIMB_BY_POSE.items():
    _ = lambda s: s.replace('-', ' ').title()
    print(limb)
    # pose, new = Pose.objects.get_or_create(name=_(slug), limb=limb, slug=slug)
    # if new:
    #     print('New pose:', pose)
