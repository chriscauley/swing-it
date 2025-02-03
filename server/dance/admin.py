from django.contrib import admin
from .models import Bar, Pose

@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    pass

@admin.register(Pose)
class PoseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'limb']
