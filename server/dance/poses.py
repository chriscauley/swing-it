from django.db import models

from collections import defaultdict

_choices = lambda x: list(zip(x,x))

ALL_POSES = []
LIMB_BY_POSE = {}

LIMBS = [
    'right-arm',
    'left-arm',
    'right-leg',
    'left-leg',
    'torso',
    'facing',
]

ARM_POSES = [
    # OUT_HEART
    "chin",
    "backpack",
    "elbows",
    "cast",
    "swing",

    # FMOON
    "sky",
    "out",
    "earth",
    "chest",

    "fmoulinet",
    "bmoulinet",
    "wing", # "air-plane" arms
    "plank", # pushup

    # dumbell poses
    "curlup",
    "curldown",
    "hammerup",
    "hammerdown",
    "punch",
    "sideup",
    "sidedown",
    "serve",
    "fisthip",
]

_is_arm = defaultdict(bool)
for pose in ARM_POSES:
    _is_arm[pose] = True
    for side in ['right', 'left']:
        slug = f'{side}-{pose}'
        _is_arm[slug] = True
        ALL_POSES.append(slug)
        LIMB_BY_POSE[slug] = f'{side}-arm'

LEG_POSES = [
    "march",
    "stand",
    "skate",
    "back", # knee up or "high" lunge
    "knee", # knee down or "tabletop"
    "tree",
    "squat",
]

_is_leg = defaultdict(bool)
for pose in LEG_POSES:
    _is_leg[pose] = True
    for side in ['right', 'left']:
        slug = f'{side}-{pose}'
        _is_leg[slug] = True
        ALL_POSES.append(slug)
        LIMB_BY_POSE[slug] = f'{side}-leg'

TORSO_POSES = [
    "cat",
    "cow",
    "neutral",
    "bowed",
    "twist",
]


FACING_POSES = [
    "audience-turn",
    "stage-turn",
]

ALL_POSES = ALL_POSES + TORSO_POSES + FACING_POSES

for pose in TORSO_POSES:
    LIMB_BY_POSE[pose] = 'torso'

for pose in FACING_POSES:
    LIMB_BY_POSE[pose] = 'facing'

LIBMS = _choices([
    "left-arm",
    "right-arm",
    "left-leg",
    "right-leg",
    "torso",
    "facing",
])
