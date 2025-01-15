from django.db import models

_choices = lambda x: list(zip(x,x))

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

ARM_POSES = [
    *LC_OUT_HEART,
    "lc_fmoulinet",
    "lc_bmoulinet",
    "lc_wing", # "air-plane" arms
    "plank", # pushup
]

LEG_POSES = [
    "march",
    "stand",
    "skate",
    "back", # knee up or "high" lunge
    "knee", # knee down or "tabletop"
    "lc_tree",
    "squat"
]

TORSO_POSES = [
    "cat",
    "cow",
    "neutral",
    "bowed",
    "twist",
]

FACING_POSES = [
    "turn_audience",
    "turn_stage",
]

LIBMS = _choices([
    "left-arm",
    "right-arm",
    "left-leg",
    "right-leg",
    "torso",
    "facing",
])

## sample moves
LC_MOON = LC_FMOON[::-1]

LC_IN_HEART = LC_OUT_HEART[::-1]

# Glitch heart switches backpack and elbows
# result is farward cast instead of side cast
LC_GLITCH_IN_HEART = [
    "lc_chin",
    "lc_elbows",
    "lc_backpack",
    "lc_cast",
    "lc_swing",
]
LC_GLITCH_OUT_HEART = LC_GLITCH_IN_HEART[::-1]

LC_TWISTED_SPIN_MARCH = [
    "cat"
    "right-arm+lc_backpack",
    "*right-leg+lc_march",
    "left-arm+lc_wing",
]
LC_TWISTED_SPIN_SKATE = [
    "bowed",
    "right-arm+lc_wing",
    "*right-leg+lc_skate",
    "left-arm+lc_backpack",
]

LC_TWISTED_SPIN_ROTATE = [
    # should start in march, how to enforce that?
    "spin_audience",
    "right-arm+lc_sky",
    "left-arm+lc_earth",
    *LC_TWISTED_SPIN_SKATE,
]

LC_TWISTED_SPIN = [
    LC_TWISTED_SPIN_MARCH,
    LC_TWISTED_SPIN_SKATE,
    LC_TWISTED_SPIN_MARCH,
    LC_TWISTED_SPIN_SKATE,
    LC_TWISTED_SPIN_MARCH,
    LC_TWISTED_SPIN_SKATE,
    LC_TWISTED_SPIN_MARCH,

    # these two should happen in one bar
    LC_TWISTED_SPIN_ROTATE,
]

## ---- Simple spin ---- ##
LC_BACKPACK = [
    "right-leg+stand",
    "right-arm+lc_backpack",
    "left-leg+stand",
    "left-arm+lc_backpack",
]

LC_AIRPLANE = [
    "right-arm+lc_wing",
    "left-arm+lc_wing",
    "right-leg+stand",
    "left-leg+stand",
]

LC_HIGH_LUNGE = [ # "backpack lunge"
    "right-arm+lc_backpack",
    "left-arm+lc_backpack",
    "right-leg+back",
]

LC_LIZARD = [
    "right-leg+knee",
    "right-arm+lc_wing",
    "left-arm+lc_wing",
    "bowed",
]

LC_SIMPLE_SPIN = [] # twisted spin but with both arms in sync
## TODO
LC_LOW_LUNGE = [] # "lizard pose"
LC_PARALLEL_HEART = []
LC_TWISTED_OUT_HEART = [] # out hearts with phase offset
LC_TWISTED_IN_HEART = [] # in hearts with phase offset
LC_FORWARD_CAST = []
LC_SIDE_CAST = []
LC_HALF_CAST = []
LC_FOREWAD_SWING = [] # arms in back+front and rotate, eyes follow backarm
LC_SQUAT_HEART = []
MOUNTAIN_CLIMBERS = []
ELBOW_TO_KNEE = []
ELBOW_TO_KNEE_HEART = []
