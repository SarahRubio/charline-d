from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post, STATUS_CHOICES


class PostList(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = Post.objects.filter(status=STATUS_CHOICES.published).order_by("-date_created")
        return qs


class PostDetail(DetailView):
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.filter(status=STATUS_CHOICES.published)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context