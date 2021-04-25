from django.urls import path

from blog.views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('<slug>', PostDetail.as_view(), name='article-blog'),
]