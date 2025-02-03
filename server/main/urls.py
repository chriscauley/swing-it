from django.contrib import admin
from django.urls import include, path, re_path
from unrest.views import index

from dance import forms
from dance.views import limb

app_urls = [
    'play',
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/limb', limb),
    path('', include('unrest_schema.urls')),
    path('', index),
    re_path(f'^({"|".join(app_urls)})', index),
]
