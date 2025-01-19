import os;from django import setup
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
setup()

from video.models import *
Video.from_external_id('K3uWj2MpydI')