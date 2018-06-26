from django.shortcuts import render
from django.views.generic import TemplateView

class CladesHomeView(TemplateView):
    template_name = 'clades/home.html'
