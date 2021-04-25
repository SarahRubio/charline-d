from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('actualites/', include('blog.urls')),
    path('competences/', include('competences.urls')),
    path('contact/', include('contact.urls')),
    path('', include('home.urls')),
]