import os;from django import setup
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

from video.settings import *
print(Video)