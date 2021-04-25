from django.urls import path
from django.views.generic import TemplateView

from home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]