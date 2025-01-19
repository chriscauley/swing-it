from django.contrib import admin
from django.urls import path, re_path
from unrest.views import index

from dance.views import pose

app_urls = [
    'play',
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/pose/', pose),
    path('', index),
    re_path(f'^({"|".join(app_urls)})', index),
]
