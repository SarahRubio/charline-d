from django.shortcuts import render
from django.views.generic import TemplateView

from recommandations.models import Recommandation


class HomeView(TemplateView):
    
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['recommandations'] = Recommandation.objects.all()

        return context

class MentionsLegalesView(TemplateView):
    
    template_name = 'mentions_legales.html'
