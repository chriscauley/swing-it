from django.http import JsonResponse

from .poses import LIMB_BY_POSE


def pose(request):
    return JsonResponse(LIMB_BY_POSE)