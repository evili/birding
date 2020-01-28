from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from .forms import CladesSearchForm
from .models import Species

class CladesHomeView(TemplateView):
    template_name = 'clades/home.html'


class CladesSearchView(FormMixin, TemplateView):
    template_name = 'clades/search.html'
    form_class = CladesSearchForm
    success_url = reverse_lazy('clades-search')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        search_items = form.cleaned_data['search'].lower().split(' ')
        obj_list  = []
    
        for si in search_items:
            obj_list.extend(
                Species.objects.filter(
                    name__icontains=si).distinct().order_by('pk'))
            obj_list.extend(
                Species.objects.filter(
                    genus__name__icontains=si).distinct().order_by('pk')
            )

        kwargs= {}
        context = self.get_context_data(**kwargs)
        context['search_results'] = obj_list
        
        response =  self.render_to_response(context, **kwargs)
        return response

    form_valid.alters_data = True
