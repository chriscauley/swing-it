from dance import poses

## sample moves
FMOON = [
    "sky",
    "out",
    "earth",
    "chest",
]
BMOON = FMOON[::-1]

OUT_HEART = [
    "chin",
    "backpack",
    "elbows",
    "cast",
    "swing",
]
IN_HEART = OUT_HEART[::-1]

# Glitch heart switches backpack and elbows
# result is farward cast instead of side cast
GLITCH_IN_HEART = [
    "chin",
    "elbows",
    "backpack",
    "cast",
    "swing",
]
GLITCH_OUT_HEART = GLITCH_IN_HEART[::-1]

TWISTED_SPIN_MARCH = [
    "cat"
    "right-arm+backpack",
    "*right-leg+march",
    "left-arm+wing",
]
TWISTED_SPIN_SKATE = [
    "bowed",
    "right-arm+wing",
    "*right-leg+skate",
    "left-arm+backpack",
]

TWISTED_SPIN_ROTATE = [
    # should start in march, how to enforce that?
    "spin_audience",
    "right-arm+sky",
    "left-arm+earth",
    *TWISTED_SPIN_SKATE,
]

TWISTED_SPIN = [
    TWISTED_SPIN_MARCH,
    TWISTED_SPIN_SKATE,
    TWISTED_SPIN_MARCH,
    TWISTED_SPIN_SKATE,
    TWISTED_SPIN_MARCH,
    TWISTED_SPIN_SKATE,
    TWISTED_SPIN_MARCH,
    TWISTED_SPIN_ROTATE,
]

## ---- Simple spin ---- ##
BACKPACK = [
    "right-leg+stand",
    "right-arm+backpack",
    "left-leg+stand",
    "left-arm+backpack",
]

AIRPLANE = [
    "right-arm+wing",
    "left-arm+wing",
    "right-leg+stand",
    "left-leg+stand",
]

HIGH_LUNGE = [ # "backpack lunge"
    "right-arm+backpack",
    "left-arm+backpack",
    "right-leg+back",
]

LOW_LUNGE = [
    "right-leg+knee",
    "right-arm+wing",
    "left-arm+wing",
    "bowed",
]

SIMPLE_SPIN = [ # twisted spin but with both arms in sync
    BACKPACK,
    AIRPLANE,
    HIGH_LUNGE,
    LOW_LUNGE,
    HIGH_LUNGE,
    AIRPLANE,
]


## TODO
PARALLEL_HEART = []
TWISTED_OUT_HEART = [] # out hearts with phase offset
TWISTED_IN_HEART = [] # in hearts with phase offset
FORWARD_CAST = []
SIDE_CAST = []
HALF_CAST = []
FOREWAD_SWING = [] # arms in back+front and rotate, eyes follow backarm
SQUAT_HEART = []
MOUNTAIN_CLIMBERS = []
ELBOW_TO_KNEE = []
ELBOW_TO_KNEE_HEART = []

if name === '__main__':
    import os, django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
    django.setup()

    from dance.models import Pose

    for pose in ALL_POSES:
        Pose.objects.get_or_create(
            slug=pose,
            name=pose.replace('-', ' ').title()
            limb=LIMB_BY_POSE[pose],
        )
