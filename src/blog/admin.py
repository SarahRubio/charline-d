from django import forms
from django.contrib import admin

from blog.models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    fields = [
        'title', 'slug', 'author', 'text', 'status', 'date_created'
    ]
    search_fields = ['title']
    list_filter = ['title', 'status', 'author']


admin.site.register(Post, PostAdmin)
