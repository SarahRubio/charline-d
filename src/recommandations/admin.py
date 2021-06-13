from django import forms
from django.contrib import admin

from recommandations.models import Recommandation

class RecommandationAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'author', 'text'
    ]
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Recommandation, RecommandationAdmin)