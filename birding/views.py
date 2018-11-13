from django.http import HttpResponse
from django.views.generic.base import View

class HealthView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('OK')

