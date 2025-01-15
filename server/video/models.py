from django.db import models

import requests
from pyquery import PyQuery as pq

_choices = lambda z: list(zip(z,z))


class Channel(models.Model):
    youtube_id = models.CharField(max_length=24, null=True, blank=True)
    twitch_id = models.CharField(max_length=24, null=True, blank=True)
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to="channel_icons")
    __str__ = lambda self: self.name


class Video(models.Model):
    __str__ = lambda self: self.title
    class Meta:
        ordering = ('order',)

    SOURCES = _choices(['youtube'])
    source = models.CharField(max_length=16, choices=SOURCES, default="youtube")
    thumbnail = models.ImageField(upload_to="video_thumbnails", null=True, blank=True)
    external_id = models.CharField(max_length=24)
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=64, null=True, blank=True)
    channel = models.ForeignKey(Channel, models.CASCADE)
    def default_data():
        return {
            'items': [],
            'room_xys': [],
        }
    data = models.JSONField(default=default_data, blank=True)

    @property
    def video_url(self):
        if self.source == 'youtube':
            return f'https://www.youtube.com/watch?v={self.external_id}'
        raise NotImplementedError('Currently only supports youtube videos')

    @property
    def channel_name(self):
        return self.channel.name

    @property
    def channel_icon(self):
        return self.channel.icon.url

    @property
    def thumbnail_url(self):
        return self.thumbnail.url

    def curl_youtube(self):
        text = requests.get(self.video_url).text
        doc = pq(text)
        for script in text.split('<script'):
            print(script.split('/script')[0]
