from django.http import JsonResponse

from .poses import LIMBS


def limb(request):
    return JsonResponse({'data': LIMBS})