from django.shortcuts import render
from django.views.generic import ListView, DetailView

from competences.models import Competence


class CompetenceList(ListView):
    template_name = 'competences/competences_list.html'
    context_object_name = 'competences'

    def get_queryset(self):
        qs = Competence.objects.all()
        return qs

class CompetenceDetail(DetailView):
    template_name = 'competences/competence_detail.html'
    context_object_name = 'competence'
    queryset = Competence.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context