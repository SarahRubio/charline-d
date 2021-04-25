from django import forms
from django.contrib import admin

from competences.models import Competence

class CompetenceAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'description'
    ]
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Competence, CompetenceAdmin)
